from flask import request, flash, render_template, jsonify
from flask_login import current_user, login_required

@login_required
def customers():
    return render_template("admin/customers.html")
