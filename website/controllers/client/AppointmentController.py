from flask import render_template, request, jsonify
from website.models import db, Service, Customer, Appointment
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
from sqlalchemy import and_

def appointmet():
    # if request.method == 'POST':
    all_services = Service.query.all()
    return render_template("client/appointment.html", services=all_services)

def clientLogin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    customer = Customer.query.filter_by(email=email).first()

    if customer and check_password_hash(customer.password, password):
        return jsonify({'message': customer.id}), 200
    else:
        return jsonify({'message': 'error'}), 401


def datepicker():
    if request.method == 'POST':
        appointments = Appointment.query.all()

        # Transformă lista de obiecte SQLAlchemy într-o listă de dicționare
        appointments_list = []
        for appointment in appointments:
            appointment_dict = {
                'id': appointment.id,
                'idCustomer': appointment.idCustomer,
                'idService': appointment.idService,
                'idStaff': appointment.idStaff,
                'notes': appointment.notes,
                'datetime': appointment.datetime.strftime('%Y-%m-%d %H:%M:%S'),  # Convertiți în format de data și oră
                'duration': appointment.duration,
                'state': appointment.state
            }
            appointments_list.append(appointment_dict)

        # Returnați lista de dicționare sub forma unui răspuns JSON
        return jsonify(appointments_list)


        # selected_date = request.form.get('selectedDate')  # Primește data selectată de la client
        # # Transformă data selectată într-un obiect datetime (poate fi necesară conversia în funcție de format)
        # selected_datetime = datetime.strptime(selected_date, '%Y-%m-%d %H:%M:%S')