# -*-coding:utf-8 -*-


from lemonbook import app
from lemonbook.models.user_models import User,Anonymous
from lemonbook import loginmanager


import index
import user
import notes


'''
提供一个user_loader回调，这个回调用于从会话中存储的用户id重新加载用户对象
接收一个用户id，并返回用户对象
当id无效时，返回None
'''
@loginmanager.user_loader
def load_user(user_id):
    #返回User类型的对象
    return User.query_by_id(user_id)

#:用户在未登入的情况下试图访问一个login_required的试图时，会重定向到登陆页面
loginmanager.login_view = "login"
loginmanager.anonymous_user = Anonymous
