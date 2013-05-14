from flask import Flask
#from lemonbook.extensions.flask_login import LoginManager

# --create app--
app = Flask(__name__)
app.config.from_object('lemonbook.config')

#login_manager = LoginManager()
#login_manager.init_app(app)


import views
