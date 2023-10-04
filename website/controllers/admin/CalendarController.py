from flask import request, flash, render_template, jsonify
from flask_login import current_user, login_required
from website.models import db, Appointment

@login_required
def adminHome():
    all_appointments = Appointment.query.all()
    return render_template("admin/home.html", appointmets=all_appointments)