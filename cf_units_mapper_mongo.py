#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ritesh Pradhan
# @Date:   2016-03-21 11:28:25
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-03-21 12:54:34


from flask import Flask, render_template, request, jsonify, redirect, url_for, Response
import os
import json
from bson import json_util
import time
import operator

from libs import libmongo
from bson.objectid import ObjectId


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

####################################
"""Read sweet_cf from db """
db = libmongo.get_db()  #db contains sweet_cf collection
db_table_name = "sweet_cf"
###########################
"""REST API"""
def to_json(data):
    """Convert Mongo object(s) to JSON"""
    return json.dumps( data, indent = 4, ensure_ascii = False )

def get_result(result):
    result["id"] = str(result["_id"])
    del result["_id"]
    return result

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

@app.route('/service/<keyword>', methods=['GET'])
def rest_service(keyword):
    """Return a list of all UFO sighting; you know what i mean
    ex) GET /service/<keyword>
    """
    try:
        if request.method == 'GET':
            results = db[db_table_name].find()
            json_results = []
            for result in results:
                json_results.append(get_result(result))
            js = to_json(json_results)
            resp = Response(js, status=200, mimetype='application/json')
            return resp
    except Exception, e:
        print (e)
        return not_found()


# @app.route("/service")
# def rest_service_key():
#     """Return specific UFO sighting which is not possible in this case
#     ex) GET /service?cf=123456
#     """
#     try:
#         if request.method == 'GET':
#             if not request.query_string:
#                 return not_found()
#             if "cf" not in set(request.args) and "units" not in set(request.args):
#                 return not_found()

#             arg_key = "cf" if "cf" in request.args else "units"
#             arg_value = request.args.get(arg_key)
#             results = db[db_table_name].find({arg_key: arg_value})
#             json_results = []
#             for result in results:
#                 json_results.append(get_result(result))
#             js = to_json(json_results)
#             resp = Response(js, status=200, mimetype='application/json')
#             return resp
#     except Exception, e:
#         print (e)
#         return not_found()


@app.route("/service")
def rest_service_key():
    """Return specific UFO sighting which is not possible in this case
    ex) GET /service?cf=123456&units=kg m-2 s-1
    """
    try:
        if request.method == 'GET':
            if not request.query_string:
                return not_found()

            params_dict = request.args.to_dict(flat=True)
            results = db[db_table_name].find(params_dict)
            json_results = []
            for result in results:
                json_results.append(get_result(result))
            js = to_json(json_results)
        resp = Response(js, status=200, mimetype='application/json')
        return resp
    except Exception, e:
        print (e)
        return not_found()


# Index page
@app.route('/')
def index():
    result = {
    "..url/service/cf-units": "for all cf and units map",
    "..url/service?cf=value": "for each cf to units map",
    "..url/service?units=value": "for each unit to cf map",
    }
    js = to_json(result)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug = False)