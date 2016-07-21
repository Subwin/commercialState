from ..models import Product

from . import main
from . import current_user

from flask import request
from flask import jsonify
from flask import abort

'''
POST /api/product/add
{
    'name': 'camera',
    'price': 100,
    'cover_url': '/static/covers/1.jpg'
}
'''


@main.route('/product/add', methods=['POST'])
def product_add():
    # u = current_user()
    form = request.get_json()
    p = Product(form)
    p.save()
    r = dict(
        success=True,
        data=p.json(),
    )
    return jsonify(r)

'''
GET /api/products
[
{
    'name': 'camera',
    'price': 100,
    'cover_url': '/static/covers/1.jpg'
}
]

'''


@main.route('/products', methods=['GET'])
def product_list():
    ps = Product.query.all()
    r = dict(
        success=True,
        data=[p.json() for p in ps],
    )
    return jsonify(r)


@main.route('/products/delete/<product_id>', methods=['GET'])
def product_delete(product_id):
    p = Product.query.filter_by(id=product_id).first()
    p.delete()
    r = dict(
        success=True,
        data='删除成功',
    )
    return jsonify(r)


# TODO
# get
# delete
# update
