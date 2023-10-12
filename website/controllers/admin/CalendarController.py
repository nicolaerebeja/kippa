from flask import request, flash, render_template, jsonify, redirect, url_for
from flask_login import current_user, login_required
from website.models import db, Appointment
import traceback

@login_required
def adminHome():
    if request.method == 'POST':
        try:
            appointment_id = request.form.get('ididAppointment')
            noteIntervento = request.form.get('noteIntervento')

            appointment = Appointment.query.get(appointment_id)

            if appointment:
                if appointment.state == 'new':
                    appointment.state = 'in progress'
                elif appointment.state == 'in progress':
                    appointment.state = 'answered'

                appointment.noteStaff = noteIntervento

                db.session.commit()

                return redirect(url_for('views.adminHome'))
            else:
                return jsonify({'message': 'Error'}), 404

        except Exception as e:
            return jsonify({'message': 'Error', 'error_details': str(e)}), 500

    all_appointments = Appointment.query.all()
    return render_template("admin/home.html", appointmets=all_appointments)