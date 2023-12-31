#!/usr/bin/python3
"""
Route for status
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def api_status():
    """
    return Ok
    """
    response = {"status": "OK"}
    return jsonify(response)


@app_views.route('/stats', methods=['GET'])
def api_stats():
    """
    return count
    """
    response = {"amenities": storage.count("Amenity"),
                "cities": storage.count("City"),
                "places": storage.count("Place"),
                "reviews": storage.count("Review"),
                "states": storage.count("State"),
                "users": storage.count("User")}
    return jsonify(response)
