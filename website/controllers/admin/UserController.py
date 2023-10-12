from flask import request, flash, render_template, jsonify, redirect, url_for
from flask_login import current_user, login_required

from website.models import db, User

@login_required
def userIndex():
    all_users = User.query.all()
    return render_template("admin/users.html", users=all_users)