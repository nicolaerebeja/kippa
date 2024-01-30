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
    #
    # if product:
    #     # Afișează toate atributele obiectului 'product' în consolă
    #     print(f"ID: {product.id}")
    #     print(f"Title: {product.title.encode('utf-8')}")
    #     print(f"Category ID: {product.category_id}")
    #     print(f"Description: {product.description.encode('utf-8')}")
    #     # ... adaugă aici și alte atribute

    return render_template("client/product.html", product=product)
