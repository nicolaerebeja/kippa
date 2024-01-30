from flask import Blueprint

from .controllers.admin.AdminHomeController import adminHome
from .controllers.admin.UserController import userIndex
from .controllers.admin.ProductController import add_product, add_category

from .controllers.HomeController import home, search_by_category, product

views = Blueprint('views', __name__)

views.route('/admin', methods=['GET', 'POST'])(adminHome)
views.route('/admin/users', methods=['GET', 'POST'])(userIndex)

views.route('/admin/add_product', methods=['GET', 'POST'])(add_product)
views.route('/admin/add_category', methods=['GET', 'POST'])(add_category)


views.route('/', methods=['GET', 'POST'])(home)
views.route('/categorie-produs/<slug>', methods=['GET'])(search_by_category)
views.route('/produs/<slug>', methods=['GET'])(product)








