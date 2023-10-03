from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from website.models import db, Service

customer_controller = Blueprint("customer_controller", __name__)

@login_required
def service():
    if request.method == 'POST':
        name = request.form.get('name')
        duration = request.form.get('duration')

        new_service = Service(name=name, duration=duration)
        db.session.add(new_service)
        db.session.commit()

    all_services = Service.query.all()
    return render_template("admin/services.html", services=all_services)
