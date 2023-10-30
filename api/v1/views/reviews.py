#!/usr/bin/python3
"""
Route for status
"""
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.review import Review


@app_views.route('/reviews', methods=['GET'])
def api_reviews_list():
    """
    return Ok
    """
    reviews = storage.all(Review).values()
    response = []
    for review in reviews:
        response.add(review.to_dict())
    return jsonify(response)


@app_views.route('/reviews/<review_id>', methods=['GET'])
def api_reviews(review_id):
    """
    return review
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    response = (review.to_dict())
    return jsonify(response)


@app_views.route('/reviews/<review_id>', methods=['DELETE'])
def api_reviews_delete(review_id):
    """
    return review
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    storage.delete(review)
    storage.save(review)
    response = {}, 200
    return jsonify(response)


@app_views.route('/reviews', methods=['POST'])
def api_reviews_add(review_id):
    """
    return add review
    """

    response = {}, 200
    return jsonify(response)


@app_views.route('/reviews/<review_id>', methods=['DELETE'])
def api_reviews_update(review_id):
    """
    return update review
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    response = {}, 200
    return jsonify(response)
