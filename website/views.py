from flask import Blueprint

from .controllers.admin.AdminHomeController import adminHome
from .controllers.admin.UserController import userIndex

from .controllers.HomeController import home

views = Blueprint('views', __name__)

views.route('/admin', methods=['GET', 'POST'])(adminHome)
views.route('/admin/users', methods=['GET', 'POST'])(userIndex)


views.route('/', methods=['GET', 'POST'])(home)



