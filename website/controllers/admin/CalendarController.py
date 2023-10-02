from flask import request, flash, render_template, jsonify
from flask_login import current_user, login_required

@login_required
def adminHome():
    return render_template("admin/home.html")
