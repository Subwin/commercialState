from . import db
from . import ReprMixin

import time


class Product(db.Model, ReprMixin):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.Integer)
    name = db.Column(db.String())
    price = db.Column(db.Integer, default=0)
    likes = db.Column(db.Integer, default=0)
    owns = db.Column(db.Integer, default=0)
    # 封面图片
    cover_url = db.Column(db.String())
    # 外键关联
    # comments = db.relationship('Comment', backref='product')

    def __init__(self, form):
        super(Product, self).__init__()
        self.name = form.get('name', '')
        self.price = int(form.get('price', 0))
        self.cover_url = form.get('cover_url', '')
        self.created_time = int(time.time())

    def json(self):
        # Model 是延迟载入的, 如果没有引用过数据, 就不会从数据库中加载
        # 引用一下 id 这样数据就从数据库中载入了
        self.id
        d = {k:v for k,v in self.__dict__.items() if k not in self.blacklist()}
        return d

    def blacklist(self):
        b = [
            '_sa_instance_state',
        ]
        return b

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
