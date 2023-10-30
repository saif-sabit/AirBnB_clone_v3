#!/usr/bin/python3
"""
Route for status
"""
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.city import City


@app_views.route('/cities', methods=['GET'])
def api_cities_list():
    """
    return Ok
    """
    cities = storage.all(City).values()
    response = []
    for city in cities:
        response.add(city.to_dict())
    return jsonify(response)


@app_views.route('/cities/<city_id>', methods=['GET'])
def api_cities(city_id):
    """
    return city
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    response = (city.to_dict())
    return jsonify(response)


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def api_cities_delete(city_id):
    """
    return city
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    storage.save(city)
    response = {}, 200
    return jsonify(response)


@app_views.route('/cities', methods=['POST'])
def api_cities_add(city_id):
    """
    return add city
    """

    response = {}, 200
    return jsonify(response)


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def api_cities_update(city_id):
    """
    return update city
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    response = {}, 200
    return jsonify(response)
