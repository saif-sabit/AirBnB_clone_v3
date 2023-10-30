#!/usr/bin/python3
"""
Route for status
"""
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'])
def api_states_list():
    """
    return Ok
    """
    states = storage.all(State).values()
    response = []
    for state in states:
        response.add(state.to_dict())
    return jsonify(response)


@app_views.route('/states/<state_id>', methods=['GET'])
def api_states(state_id):
    """
    return state
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    response = (state.to_dict())
    return jsonify(response)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def api_states_delete(state_id):
    """
    return state
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save(state)
    response = {}, 200
    return jsonify(response)


@app_views.route('/states', methods=['POST'])
def api_states_add(state_id):
    """
    return add state
    """

    response = {}, 200
    return jsonify(response)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def api_states_update(state_id):
    """
    return update state
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    response = {}, 200
    return jsonify(response)
