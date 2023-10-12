from flask import Blueprint, render_template, request, flash, redirect, url_for ,jsonify
from flask_login import login_required, current_user
from website.models import db, Service

customer_controller = Blueprint("customer_controller", __name__)

@login_required
def service():
    if request.method == 'POST':
        name = request.form.get('name')
        duration = request.form.get('duration')

        newName = request.form.get('newName')
        newDuration = request.form.get('newDuration')

        type = request.form.get('type')

        id = request.form.get('id')
        if type:
            service = Service.query.get(id)

            if service:
                db.session.delete(service)
            else:
                return jsonify({'message': 'Service not found'}), 404

        elif id:
            service = Service.query.get(id)

            if service:
                service.name = newName
                service.duration = newDuration
            else:
                return jsonify({'message': 'Service not found'}), 404

        else:
            new_service = Service(name=name, duration=duration)
            db.session.add(new_service)

        db.session.commit()

    all_services = Service.query.all()
    return render_template("admin/services.html", services=all_services)
