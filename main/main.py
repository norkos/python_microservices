from dataclasses import dataclass

import requests
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

import producer

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://norkos:norkos@db/main'
CORS(app)

db = SQLAlchemy(app)

@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/api/products')
def index():
    return jsonify(Product.query.all())


@app.route('/api/products/<int:product_id>/like', methods=['POST'])
def like(product_id):

    try:
        resp = requests.get('http://host.docker.internal:8000/api/user')
        resp.raise_for_status()
    except requests.exceptions.HTTPError as err:
        return jsonify({
            'message': err.response.status_code
        })

    json = resp.json()

    try:
        product_user = ProductUser(user_id=json['id'], product_id=product_id)
        db.session.add(product_user)
        db.session.commit()

        producer.publish('product_liked', product_id)
    except Exception as e:
        abort(400, 'You already liked this product')

    return jsonify({
        'message': "Success"
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
