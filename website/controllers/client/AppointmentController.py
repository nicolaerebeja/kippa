from flask import render_template, request, jsonify

from website.controllers.admin.EmailController import send_email
from website.models import db, Service, Customer, Appointment
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
from sqlalchemy import func
from urllib.parse import unquote

# import logging
#
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


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
        customer_data = {
            'id': customer.id,
            'name': customer.name,
            'surname': customer.surname,
            'email': customer.email
        }

        return jsonify({'customer': customer_data}), 200
    else:
        return jsonify({'message': 'error'}), 401


def datepicker():
    if request.method == 'POST':
        selectedDate = request.form.get('selectedDate') # mi prendo la data sezionata dal cliente
        # selectedDate: 2023-10-05 // questo e il formato
        try:
            appointment_datetime = datetime.strptime(selectedDate, "%Y-%m-%d") # provo a confertirla per il db
        except ValueError:
            return jsonify({'message': 'Invalid date or time format'}), 400

        appointment_date = appointment_datetime.date() # dopo la conversione si e aggiunto anche l'ora, quindi mi prendo solo il giorno

        # eseguo query che peschi tutti gli appuntamenti di quel giorno
        appointments = db.session.query(Appointment).filter(
            func.date(Appointment.datetime) == appointment_date
        ).all()

        appointment_hours = [] # mi creo una lista per mettere solo le ore gia occupate

        for appointment in appointments:
            hour = appointment.datetime.strftime("%H") # prendo da dataora solo l'ora
            appointment_hours.append(int(hour)) # la aggiungo alla lista

        available_time_day = [9, 10, 11, 14, 15] # questa e la lista del orarrio disponibile per appti.

        available_time = [x for x in available_time_day if x not in appointment_hours] # tolgo le ore gia occupate


        return jsonify(available_time)



def newAppointmet():
    if request.method == 'POST':
        data = request.get_json()
        emailCliente = data.get('emailCliente')
        servizioCliente = data.get('servizioCliente')
        dataCliente = data.get('dataCliente')
        orarioCliente = data.get('orarioCliente')
        noteCliente = data.get('noteCliente')
        recapitoCliente = data.get('recapitoCliente')

        # 1. Obțineți id-ul clientului pe baza adresei de email
        customer = Customer.query.filter_by(email=emailCliente).first()

        if not customer:
            return jsonify({'message': 'Client not found'}), 400

        # 2. Obțineți durata serviciului pentru serviciul selectat
        service = Service.query.get(servizioCliente)
        if not service:
            return jsonify({'message': 'Service not found'}), 400

        duration = service.duration

        # 3. Combinați data și orarul pentru a forma un obiect datetime
        # (asigurați-vă că formatul datei și orarului este potrivit)
        try:
            appointment_datetime = datetime.strptime(f"{dataCliente} {orarioCliente}", "%d/%m/%Y %H")
                                                            #     5/10/2023 14
        except ValueError:
            return jsonify({'message': 'Invalid date or time format'}), 400

        # 4. Introduceți datele în baza de date
        new_appointment = Appointment(
            idCustomer=customer.id,
            idService=servizioCliente,
            notes=noteCliente,
            datetime=appointment_datetime,
            duration=duration,
            recapito=recapitoCliente,
            state='new',
            noteStaff=''
        )

        db.session.add(new_appointment)
        db.session.commit()

        subject = 'Sol30 - Conferma richiesta appuntamento'
        message = f'Le confermiamo che la sua richiesta per l\'appuntamento del {dataCliente} alle ore {orarioCliente}:00 è stata correttamente inviata.\n\nServizio richiesto: {service.name}'

        send_email(customer.email, subject, message)

        # itexpertEmail='itexpert.vodafone@solutions30.com'
        itexpertEmail='pretulcorect.com@gmail.com'
        subjectStaff = 'Sol30 - Nuova richiesta appuntamento'
        messageStaff = f'Hai ricevuto una nuova prenotazione da un cliente.\n\nDati del cliente:\nNome: {customer.name}\nCognome: {customer.surname}\nEmail: {customer.email}\nTelefono Cliente: {customer.tel}\nRecapito Appuntamento: {recapitoCliente}\n\nDettagli della prenotazione:\nData: {dataCliente}\nOra: {orarioCliente}:00\nServizio richiesto: {service.name}\nNote: {noteCliente}'

        send_email(itexpertEmail, subjectStaff, messageStaff)

        return jsonify({'message': 'Appointment added successfully'}), 201

    return jsonify({'message': 'Method not allowed'}), 405