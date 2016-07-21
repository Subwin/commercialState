from ..models import Article

from . import main
from . import current_user

from flask import request
from flask import jsonify
from flask import abort

'''
POST /api/article/add
{
    'name': 'camera',
    'title': 'Notebook holder;',
    'content': 'Notebook holder is very good and useful.',
    'author': 'subwin',
    'cover_url': '/static/covers/1.jpg'
}
'''


@main.route('/article/add', methods=['POST'])
def article_add():
    # u = current_user()
    form = request.get_json()
    a = Article(form)
    a.save()
    r = dict(
        success=True,
        data=p.json(),
    )
    return jsonify(r)

'''
GET /api/articles
[
{
    'name': 'camera',
    'price': 100,
    'cover_url': '/static/covers/1.jpg'
}
]

'''


@main.route('/articles', methods=['GET'])
def passage_list():
    ats = Article.query.all()
    r = dict(
        success=True,
        data=[p.json() for p in ats],
    )
    return jsonify(r)

#
# @main.route('/products/delete/<product_id>', methods=['GET'])
# def product_delete(product_id):
#     p = Product.query.filter_by(id=product_id).first()
#     p.delete()
#     r = dict(
#         success=True,
#         data='删除成功',
#     )
#     return jsonify(r)


# TODO
# get
# delete
# update