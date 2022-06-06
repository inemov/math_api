#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 22:01:11 2022

@author: Ivan Nemov
"""


from flask import Flask, request, jsonify
from waitress import serve
import json


def createApp():
    """
    Flask Application
    """
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        """
        API index page
        """
        return 'Test Flask-based Web API with math functions.'

    @app.route('/square', methods=['POST'])
    def square():
        """
        Return square of posted number
        """
        req = request.get_json()
        if (not req):
            return 'JSON is incorrect.'

        # check payload
        try:
            payload = json.loads(req)
        except:
            payload = None
        
        # if not provided
        if (not payload):
            return 'JSON is empty.'

        # calculate square
        try:
            res = pow(float(payload['val']), 2)
        except:
            return 'Value is not provided or cannot be casted to float type.'

        return jsonify({'res': res})

    return app


if __name__ == '__main__':
    """
    Entry point
    """
    app = createApp()

    # start web server
    serve(app, host="0.0.0.0", port=5005)