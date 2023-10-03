from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from website.models import db, Appointment
from website.controllers.admin.EmailController import send_email

import random
import string

customer_controller = Blueprint("customer_controller", __name__)

@login_required
def appointmets():
    # if request.method == 'POST':


    all_appointments = Appointment.query.all()
    return render_template("admin/appointmets.html", appointmets=all_appointments)
