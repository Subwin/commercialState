from ..models import User
from ..models import Tweet
from . import main
from . import current_user

from flask import request
from flask import jsonify


@main.route('/tweet/add', methods=['POST'])
def tweet_add():
    u = current_user()
    form = request.get_json()
    t = Tweet(form)
    t.user = u
    t.save()
    r = dict(
        success=True,
        data=t.json(),
    )
    return jsonify(r)

# TODO
# delete
# update
