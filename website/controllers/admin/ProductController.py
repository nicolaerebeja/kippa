import os

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms import StringField, FloatField, IntegerField, TextAreaField
from wtforms.validators import DataRequired

import app
from website import db
from website.models import Product, Category


def add_product():
    if request.method == 'POST':
        title = request.form.get('title')
        category_id = request.form.get('category_id')
        description = request.form.get('description')
        price = request.form.get('price')
        discount = request.form.get('discount', 0)
        details = request.form.get('details')
        # main_image = request.form.get('main_image')

        main_image = request.files['main_image']
        if main_image and allowed_file(main_image.filename):
            filename = secure_filename(main_image.filename)
            image_folder = 'client/product_images'  # Modifică în funcție de structura folderelor tale
            image_path = os.path.join('website', 'static', image_folder, filename)
            main_image.save(image_path)

            # Construiește manual URL-ul folosind calea relativă
            main_image_url = f'/static/{image_folder}/{filename}'
        else:
            main_image_url = None

        print(main_image)
        # other_images = request.form.get('other_images')

        # if title and category_id and description and price and details and main_image:
        price = float(price)
        discount = float(discount)

        new_product = Product(
            title=title,
            category_id=category_id,
            description=description,
            price=price,
            discount=discount,
            details=details,
            main_image=main_image_url,
        )

        db.session.add(new_product)
        db.session.commit()

        return render_template('admin/products/create.html')

    else:
        all_categories = Category.query.all()

        return render_template('admin/products/create.html', categories=all_categories)


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def add_category():
    if request.method == 'POST':
        name = request.form.get('title')

        new_category = Category(
            name=name
        )

        db.session.add(new_category)
        db.session.commit()

        return render_template('admin/category/index.html')
    else:
        return render_template('admin/category/create.html')
