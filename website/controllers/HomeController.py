from flask import request, flash, render_template, jsonify

def home():
    return render_template("client/home.html")
