from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///click_and_cart.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'

db = SQLAlchemy(app)

products = [
    {"id": 1, "name": "Laptop", "price": "$800", "image": "laptop.jpg"},
    {"id": 2, "name": "Smartphone", "price": "$500", "image": "smartphone.png"},
    {"id": 3, "name": "Headphones", "price": "$100", "image": "headphones.jpg"}
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return render_template('product.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []

    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        session['cart'].append(product)
        session.modified = True

    cart_html = render_template('cart_items.html', cart_items=session['cart'])
    return jsonify(cart_html=cart_html)

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    return render_template('cart.html', cart_items=cart_items)

if __name__ == '__main__':
    app.run(debug=True)
