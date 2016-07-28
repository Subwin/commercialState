import requests
import random
import json


def random_product():
    price = random.randint(0, 1000)
    i = random.randint(0,3)
    p = {
        'name': '{}'.format(product[i]),
        'price': price,
        'cover_url': '/static/covers/1.jpg'
    }
    return p

# POST /api/product/add
# {
#     'name': 'camera',
#     'price': 100,
#     'cover_url': '/static/covers/1.jpg'
# }

host = 'http://127.0.0.1:5000'
product = ['camera', 'phone', 'notebook', 'cup']
author = ['subwin', 'gua', 'jiang', 'jinping']


def post(path, form):
    url = host + path
    r = requests.post(url, json=form)
    return r


def get(path):
    url = host + path
    r = requests.get(url)
    return r


def product_add():
    path = '/api/product/add'
    form = random_product()
    post(path, form)


def formated_json(obj):
    return json.dumps(obj, indent=2)


def product_list():
    path = '/api/products'
    r = get(path)
    response = r.json()
    data = response['data']
    print(r, len(data))
    for d in data:
        print(formated_json(d))


# POST /api/product/add
# {
#     'name': 'camera',
#     'title': 'Notebook holder;',
#     'content': 'Notebook holder is very good and useful.',
#     'author': 'subwin',
#     'cover_url': '/static/covers/1.jpg'
# }

def random_passage():
    random_num = random.randint(0,3)
    p = {
            'name': '{}'.format(product[random_num]),
            'title': '{};'.format(product[random_num]),
            'content': '{} is very good and useful.'.format(product[random_num]),
            'author': '{}'.format(author[random_num]),
            'cover_url': '/static/covers/{}.jpg'.format(random_num)
    }
    return p


def passage_add():
    path = '/api/passage/add'
    form = random_passage()
    post(path, form)


def main():
    # product_list()
    for i in range(9):
        product_add()
    for i in range(9):
        passage_add()

if __name__ == '__main__':
    main()
