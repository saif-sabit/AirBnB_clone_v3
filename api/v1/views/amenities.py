#!/usr/bin/python3
"""
Route for status
"""
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'])
def api_amenities_list():
    """
    return Ok
    """
    amenities = storage.all(Amenity).values()
    response = []
    for amenity in amenities:
        response.add(amenity.to_dict())
    return jsonify(response)


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def api_amenities(amenity_id):
    """
    return amenity
    """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    response = (amenity.to_dict())
    return jsonify(response)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def api_amenities_delete(amenity_id):
    """
    return amenity
    """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    storage.save(amenity)
    response = {}, 200
    return jsonify(response)


@app_views.route('/amenities', methods=['POST'])
def api_amenities_add(amenity_id):
    """
    return add amenity
    """

    response = {}, 200
    return jsonify(response)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def api_amenities_update(amenity_id):
    """
    return update amenity
    """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    response = {}, 200
    return jsonify(response)
