#!/usr/bin/python3
""" define our route functions"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """returns a JSON status"""
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def retrive_count():
    """ an enpoint that retrives the number of each objects"""
    stats = {}
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]
    for i in len(classes):
        stats[names[i]] = storage.count(classes[i])

    return jsonify(stats)
