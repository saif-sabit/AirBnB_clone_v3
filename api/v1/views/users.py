#!/usr/bin/python3
"""
Route for status
"""
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'])
def api_users_list():
    """
    return Ok
    """
    users = storage.all(User).values()
    response = []
    for user in users:
        response.add(user.to_dict())
    return jsonify(response)


@app_views.route('/users/<user_id>', methods=['GET'])
def api_users(user_id):
    """
    return user
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    response = (user.to_dict())
    return jsonify(response)


@app_views.route('/users/<user_id>', methods=['DELETE'])
def api_users_delete(user_id):
    """
    return user
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save(user)
    response = {}, 200
    return jsonify(response)


@app_views.route('/users', methods=['POST'])
def api_users_add(user_id):
    """
    return add user
    """

    response = {}, 200
    return jsonify(response)


@app_views.route('/users/<user_id>', methods=['DELETE'])
def api_users_update(user_id):
    """
    return update user
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    response = {}, 200
    return jsonify(response)
