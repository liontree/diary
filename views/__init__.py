from lemonbook import app
from lemonbook import config
from lemonbook.extensions import login_manager
from lemonbook.models.user_models import User

import index
import user
import notes

@login_manager.user_loader
def load_user(id):
    return User().query_by_id(id)


