#!/usr/bin/python3
"""
app file
"""
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask import jsonify
app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Tears down .
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    return 404 but json
    """
    response = jsonify({"error": "Not found"})
    
    return jsonify(response), 404


if __name__ == "__main__":
    host = "0.0.0.0" if not getenv(
        "HBNB_API_HOST") else getenv("HBNB_API_HOST")
    port = 5000 if not getenv(
        "HBNB_API_PORT") else int(getenv("HBNB_API_PORT"))
    app.run(host=host, port=port, threaded=True)
