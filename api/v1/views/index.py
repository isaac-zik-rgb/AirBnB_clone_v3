#!/usr/bin/python3
""" define our route functions"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def status():
    """returns a JSON status"""
    return jsonify({"status": "OK"})
