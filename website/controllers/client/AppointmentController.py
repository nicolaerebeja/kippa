from flask import render_template, request, jsonify
from website.models import db, Service, Customer
from werkzeug.security import check_password_hash


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