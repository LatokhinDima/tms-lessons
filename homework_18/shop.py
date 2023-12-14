import sqlite3
from dataclasses import dataclass
from typing import Optional

from flask import Flask, abort, redirect, session, request
from flask_session import Session

DATABASE_FILE = 'products.db'

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@dataclass
class Product:
    id: int
    name: str
    description: str
    category: str


def load_products() -> list[Product]:
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute(
            'SELECT id, name, description, category FROM product')
        return [Product(*values) for values in execution_result.fetchall()]


def get_product(product_id: int) -> Product:
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute('SELECT id, name, description, category '
                                              'FROM product '
                                              'WHERE id = ?', (product_id,))
        rows = execution_result.fetchall()
        if len(rows) != 1:
            raise ValueError(f'Expected 1 object with id {product_id}, got {len(rows)}')
        return Product(*rows[0])


@app.route('/')
@app.route('/products')
def products_view():
    products = load_products()
    products_html = '\n'.join(
        f'<li><a href="/product/{product.id}">{product.name}</a></li>'
        for product in products)

    return f'''
    <html>
        <head>
            <title>Products APP</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
        </head>
        <body>
            <h1>All Products</h1>
            <ul>
                {products_html}
            </ul>
        </body>
    </html>
    '''


@app.route('/product/<int:product_id>')
def product_id_detail(product_id: int):
    product = get_product(product_id)
    if product is None:
        abort(404, 'Product not found')
    return f'''
    <html>
        <head>
            <title>Product APP</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
        </head>
        <body>
            <p><a href="/products">Go to home page</a></p>
            <h1>{product.name}</h1>
            <h3>Discription: {product.description} <br> Category: {product.category}</h3
            </form>
        </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(port=8080, debug=True)
