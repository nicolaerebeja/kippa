from flask import request, flash, render_template, jsonify

from website.models import Product, Category


def home():
    return render_template("client/home.html")


def search_by_category(slug):
    category_name = slug.replace('-', ' ')
    category = Category.query.filter_by(name=category_name).first()
    products = Product.query.filter_by(category_id=category.id).all()

    return render_template("client/category.html", products=products)


def product(slug):
    product_name = slug.replace('-', ' ')
    product = Product.query.filter_by(title=product_name).first()

    if product:
        # Afișează toate atributele obiectului 'product' în consolă
        print(f"d: {product.discount}")


    return render_template("client/product.html", product=product)
