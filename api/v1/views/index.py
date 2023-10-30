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
