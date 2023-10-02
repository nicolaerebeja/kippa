from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from website.models import db, Customer
import random
import string

customer_controller = Blueprint("customer_controller", __name__)

@login_required
def add_customer():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        tel = request.form.get('tel')
        piva = request.form.get('piva')
        email = request.form.get('email')

        # Generarea unei parole aleatoare pentru client
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        # Crearea unui nou obiect Customer și adăugarea lui în baza de date
        new_customer = Customer(name=name, surname=surname, tel=tel, piva=piva, email=email, password=password)
        db.session.add(new_customer)
        db.session.commit()

        flash('Customer added successfully!', category='success')
        return redirect(url_for('customer_controller.customers'))  # Redirecționează către pagina cu lista de clienți sau altă pagină relevantă

    return render_template("admin/customers.html")
