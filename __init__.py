from flask import Flask

# --create app--
app = Flask(__name__)
app.config.from_object('lemondbook.config')

import views
