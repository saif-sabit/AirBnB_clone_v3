#!/usr/bin/python3
"""
Route for status
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'])
def api_states_list():
    """
    return Ok
    """
    states = storage.all(State).values()
    response = [state.to_dict() for state in states]

    return jsonify(response)


@app_views.route('/states/<string:state_id>', methods=['GET'])
def api_states(state_id):
    """
    return state
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    response = state.to_dict()
    return jsonify(response)


@app_views.route('/states/<string:state_id>',
                 methods=['DELETE'], strict_slashes=False)
def api_states_delete(state_id):
    """
    return state
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save(state)
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def api_states_add(state_id):
    """
    return add state
    """
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if 'name' not in data:
        abort(400, description="Missing name")
    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<string:state_id>',
                 methods=['PUT'], strict_slashes=False)
def api_states_update(state_id):
    """
    return update state
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
