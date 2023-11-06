#!/usr/bin/python3
"""
Route for status
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def api_users_list():
    """
    return Ok
    """
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])


@app_views.route('/users/<user_id>',
                 methods=['GET'], strict_slashes=False)
def api_users(user_id):
    """
    return user
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    response = (user.to_dict())
    return jsonify(response)


@app_views.route('/users/<user_id>',
                 methods=['DELETE'], strict_slashes=False)
def api_users_delete(user_id):
    """
    return user
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({})


@app_views.route('/users',
                 methods=['POST'], strict_slashes=False)
def api_users_add():
    """
    return add user
    """

    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if 'email' not in data:
        return jsonify({"error": "Missing email"}), 400
    if 'password' not in data:
        return jsonify({"error": "Missing password"}), 400
    new_user = User(**data)
    new_user.save()
    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>',
                 methods=['PUT'], strict_slashes=False)
def api_users_update(user_id):
    """
    return update user
    """
    if user:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Not a JSON"}), 400
        ignore_keys = ['id', 'email', 'created_at', 'updated_at']
        for key, value in data.items():
            if key not in ignore_keys:
                setattr(user, key, value)
        user.save()
        return jsonify(user.to_dict())
    abort(404)
