from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from website.models import db, Customer
from website.controllers.admin.EmailController import send_email

import random
import string

customer_controller = Blueprint("customer_controller", __name__)

@login_required
def customers():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        tel = request.form.get('tel')
        piva = request.form.get('piva')
        email = request.form.get('email')

        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        new_customer = Customer(name=name, surname=surname, tel=tel, piva=piva, email=email, password=password)
        db.session.add(new_customer)
        db.session.commit()

        subject = 'Sol30 - Attivazione dell\'account'
        message = f'Il tuo account per il portale delle prenotazioni on-line è stato attivato.\nI dati di accesso sono i seguenti:\n\nLogin: {email}\nPassword: {password}\n\nPer visualizzare il portale accedi all\'indirizzo: sol30.com'

        send_email(email, subject, message)

    all_customers = Customer.query.all()
    return render_template("admin/customers.html", customers=all_customers)
    # return render_template("admin/customers.html")
