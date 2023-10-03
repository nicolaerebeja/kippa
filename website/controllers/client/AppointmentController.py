from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from website.models import db, Appointment
from website.controllers.admin.EmailController import send_email


def appointmet():
    # if request.method == 'POST':

    return render_template("client/appointment.html")
