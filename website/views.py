from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

from .controllers.admin.CalendarController import adminHome
from .controllers.admin.CustomersController import customers
from .controllers.admin.ServiceController import service
from .controllers.admin.AppointmentController import appointmets

from .controllers.HomeController import home

views = Blueprint('views', __name__)

views.route('/admin', methods=['GET', 'POST'])(adminHome)
views.route('/admin/customers', methods=['GET', 'POST'])(customers)
views.route('/admin/services', methods=['GET', 'POST'])(service)
views.route('/admin/appointments', methods=['GET', 'POST'])(appointmets)



views.route('/', methods=['GET', 'POST'])(home)

