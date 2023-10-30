#!/usr/bin/python3
"""
Route for status
"""
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.place import Place


@app_views.route('/places', methods=['GET'])
def api_places_list():
    """
    return Ok
    """
    places = storage.all(Place).values()
    response = []
    for place in places:
        response.add(place.to_dict())
    return jsonify(response)


@app_views.route('/places/<place_id>', methods=['GET'])
def api_places(place_id):
    """
    return place
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    response = (place.to_dict())
    return jsonify(response)


@app_views.route('/places/<place_id>', methods=['DELETE'])
def api_places_delete(place_id):
    """
    return place
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    storage.save(place)
    response = {}, 200
    return jsonify(response)


@app_views.route('/places', methods=['POST'])
def api_places_add(place_id):
    """
    return add place
    """

    response = {}, 200
    return jsonify(response)


@app_views.route('/places/<place_id>', methods=['DELETE'])
def api_places_update(place_id):
    """
    return update place
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    response = {}, 200
    return jsonify(response)
