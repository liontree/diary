# -*- coding: utf-8 -*-

import hmac
from datetime import datetime, timedelta
from flask import (current_app, session, _request_ctx_stack, redirect, url_for,
                   request, flash, abort)
from flask.signals import Namespace
from functools import wraps
from hashlib import sha1, md5
from urlparse import urlparse, urlunparse
from werkzeug.local import LocalProxy
from werkzeug.urls import url_decode, url_encode

_signals = Namespace()


def _get_user():
    return getattr(_request_ctx_stack.top, "user", None)


def _cookie_digest(payload, key=None):
    if key is None:
        key = current_app.config["SECRET_KEY"]
    payload = payload.encode("utf8")
    mac = hmac.new(key, payload, sha1)
    return mac.hexdigest()


def encode_cookie(payload):
    return u"%s|%s" % (payload, _cookie_digest(payload))


def decode_cookie(cookie):
    try:
        payload, digest = cookie.rsplit(u"|", 1)
        digest = digest.encode("ascii")
    except ValueError:
        return None
    if _cookie_digest(payload) == digest:
        return payload
    else:
        return None


def make_next_param(login, current):
    login_scheme, login_netloc = urlparse(login)[:2]
    current_scheme, current_netloc = urlparse(current)[:2]
    if ((not login_scheme or login_scheme == current_scheme) and
        (not login_netloc or login_netloc == current_netloc)):
        parsed = urlparse(current)
        return urlunparse(("", "", parsed[2], parsed[3], parsed[4], ""))
    return current


def login_url(login_view, next_url=None, next_field="next"):
    if login_view.startswith(("https://", "http://", "/")):
        base = login_view
    else:
        base = url_for(login_view)
    if next_url is None:
        return base
    parts = list(urlparse(base))
    md = url_decode(parts[4])
    md[next_field] = make_next_param(base, next_url)
    parts[4] = url_encode(md, sort=True)
    return urlunparse(parts)


def make_secure_token(*args, **options):
    key = options.get("key")
    if key is None:
        key = current_app.config["SECRET_KEY"]
    payload = "\0".join((
        s.encode("utf8") if isinstance(s, unicode) else s) for s in args
    )
    mac = hmac.new(key, payload, sha1)
    return mac.hexdigest().decode("utf8")


def _create_identifier():
    base = unicode("%s|%s" % (request.remote_addr,
                              request.headers.get("User-Agent")), 'utf8', errors='replace')
    hsh = md5()
    hsh.update(base.encode("utf8"))
    return hsh.hexdigest()


COOKIE_NAME = "remember_token"

COOKIE_DURATION = timedelta(days=365)

class LoginManager(object):
    def __init__(self):
        self.anonymous_user = AnonymousUser
        self.login_view = None
        self.refresh_view = None
        self.session_protection = "basic"
        self.token_callback = None
        self.user_callback = None
        self.unauthorized_callback = None
        self.needs_refresh_callback = None

    def user_loader(self, callback):
        self.user_callback = callback
        return callback

    def token_loader(self, callback):
        self.token_callback = callback
        return callback

    def setup_app(self, app, add_context_processor=True):
        import warnings
        warnings.warn("Warning setup_app is deprecated. Please use init_app",
                       DeprecationWarning)
        self.init_app(app, add_context_processor)

    def init_app(self, app, add_context_processor=True):
        app.login_manager = self
        app.before_request(self._load_user)
        app.after_request(self._update_remember_cookie)
        if add_context_processor:
            app.context_processor(_user_context_processor)

    def unauthorized_handler(self, callback):
        self.unauthorized_callback = callback
        return callback

    def unauthorized(self):
        user_unauthorized.send(current_app._get_current_object())
        if self.unauthorized_callback:
            return self.unauthorized_callback()
        if not self.login_view:
            abort(401)
        return redirect(login_url(self.login_view, request.url))

    def needs_refresh_handler(self, callback):
        self.needs_refresh_callback = callback
        return callback

    def needs_refresh(self):
        user_needs_refresh.send(current_app._get_current_object())
        if self.needs_refresh_callback:
            return self.needs_refresh_callback()
        if not self.refresh_view:
            abort(403)
        return redirect(login_url(self.refresh_view, request.url))

    def _load_user(self):
        if (current_app.static_url_path is not None and
            request.path.startswith(current_app.static_url_path)
        ):
            _request_ctx_stack.top.user = self.anonymous_user()
            return
        config = current_app.config
        if config.get("SESSION_PROTECTION", self.session_protection):
            deleted = self._session_protection()
            if deleted:
                self.reload_user()
                return
        cookie_name = config.get("REMEMBER_COOKIE_NAME", COOKIE_NAME)
        if cookie_name in request.cookies and "user_id" not in session:
            self._load_from_cookie(request.cookies[cookie_name])
        else:
            self.reload_user()

    def _session_protection(self):
        sess = session._get_current_object()
        ident = _create_identifier()
        if "_id" not in sess:
            sess["_id"] = ident
        elif ident != sess["_id"]:
            app = current_app._get_current_object()
            mode = app.config.get("SESSION_PROTECTION",
                                  self.session_protection)
            if mode == "basic" or sess.permanent:
                sess["_fresh"] = False
                session_protected.send(app)
                return False
            elif mode == "strong":
                sess.clear()
                sess["remember"] = "clear"
                session_protected.send(app)
                return True
        return False

    def reload_user(self):
        ctx = _request_ctx_stack.top
        user_id = session.get("user_id", None)
        if user_id is None:
            ctx.user = self.anonymous_user()
        else:
            user = self.user_callback(user_id)
            if user is None:
                logout_user()
            else:
                ctx.user = user

    def _load_from_cookie(self, cookie):
        if self.token_callback:
            user = self.token_callback(cookie)
            if user is not None:
                user_id = user.get_id()
        else:
            user_id = decode_cookie(cookie)

        if user_id is not None:
            session["user_id"] = user_id
            session["_fresh"] = False
            self.reload_user()

            app = current_app._get_current_object()
            user_loaded_from_cookie.send(app, user=_get_user())
        else:
            self.reload_user()

    def _update_remember_cookie(self, response):
        operation = session.pop("remember", None)
        if operation == "set" and "user_id" in session:
            self._set_cookie(response)
        elif operation == "clear":
            self._clear_cookie(response)
        return response

    def _set_cookie(self, response):
        # cookie settings
        config = current_app.config
        cookie_name = config.get("REMEMBER_COOKIE_NAME", COOKIE_NAME)
        duration = config.get("REMEMBER_COOKIE_DURATION", COOKIE_DURATION)
        domain = config.get("REMEMBER_COOKIE_DOMAIN", None)
        # prepare data
        if self.token_callback:
            data = current_user.get_auth_token()
        else:
            data = encode_cookie(str(session["user_id"]))
        expires = datetime.utcnow() + duration
        # actually set it
        response.set_cookie(cookie_name, data, expires=expires, domain=domain)

    def _clear_cookie(self, response):
        config = current_app.config
        cookie_name = config.get("REMEMBER_COOKIE_NAME", COOKIE_NAME)
        domain = config.get("REMEMBER_COOKIE_DOMAIN", None)
        response.delete_cookie(cookie_name, domain=domain)


current_user = LocalProxy(lambda: _request_ctx_stack.top.user)

def _user_context_processor():
    return dict(current_user=_get_user())


def login_fresh():
    return session.get("_fresh", False)


def login_user(user, remember=False):
    user_id = user.id
    session["user_id"] = user_id
    session["_fresh"] = True
    if remember:
        session["remember"] = "set"
    current_app.login_manager.reload_user()
    user_logged_in.send(current_app._get_current_object(), user=_get_user())
    return True


def logout_user():
    if "user_id" in session:
        del session["user_id"]
    if "_fresh" in session:
        del session["_fresh"]
    cookie_name = current_app.config.get("REMEMBER_COOKIE_NAME", COOKIE_NAME)
    if cookie_name in request.cookies:
        session["remember"] = "clear"
    user = _get_user()
    if user and (not user.is_anonymous()):
        user_logged_out.send(current_app._get_current_object(), user=user)
    current_app.login_manager.reload_user()
    return True


def confirm_login():
    session["_fresh"] = True
    session["_id"] = _create_identifier()
    user_login_confirmed.send(current_app._get_current_object())


def login_required(fn):
    @wraps(fn)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated():
            return current_app.login_manager.unauthorized()
        return fn(*args, **kwargs)
    return decorated_view


def fresh_login_required(fn):
    @wraps(fn)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated():
            return current_app.login_manager.unauthorized()
        elif not login_fresh():
            return current_app.login_manager.needs_refresh()
        return fn(*args, **kwargs)
    return decorated_view


class LoginRequiredMixin(object):
    @login_required
    def dispatch_request(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch_request(*args, **kwargs)


class UserMixin(object):
    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id



class AnonymousUser(object):
    def is_authenticated(self):
        return False

    def is_active(self):
        return False

    def is_anonymous(self):
        return True

    def get_id(self):
        return None


user_logged_in = _signals.signal("logged-in")

user_logged_out = _signals.signal("logged-out")

user_loaded_from_cookie = _signals.signal("loaded-from-cookie")

user_login_confirmed = _signals.signal("login-confirmed")

user_unauthorized = _signals.signal("unauthorized")

user_needs_refresh = _signals.signal("needs-refresh")

session_protected = _signals.signal("session-protected")
