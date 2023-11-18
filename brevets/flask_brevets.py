"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config

import logging

from pymongo import MongoClient
from flask import Flask, redirect, url_for, request, render_template, jsonify
import os

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()

###
# Pages
###

# Connect MongoDB
client = MongoClient("mongodb://" + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mydb

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html', items=list(db.myposts.find()))


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    brevkm = request.args.get('brevkm', type=float)
    app.logger.debug("Brevets Distance: {}".format(brevkm))
    begin = request.args.get('begin', type=str)
    app.logger.debug("Start time: {}".format(begin))
    # FIXME!
    # Right now, only the current time is passed as the start time
    # and control distance is fixed to 200
    # You should get these from the webpage!
    open_time = acp_times.open_time(km, brevkm, begin).format('YYYY-MM-DDTHH:mm')
    close_time = acp_times.close_time(km, brevkm, begin).format('YYYY-MM-DDTHH:mm')
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)

@app.route('/submit_data/', methods=['POST', 'GET'])
def submit_data():
    if request.method == 'POST':
        item_doc = {
            'distance': request.form['distance'],
            'begin_date': request.form['begin_date'],
            'km': request.form['km'],
            'miles': request.form['miles'],
            'open': request.form['open'],
            'close': request.form['close']
        }
        db.myposts.insert_one(item_doc)
        return jsonify({"message": "Data submitted successfully"})
    elif request.method == 'GET':
        return jsonify({"message": "GET not supported"})

    return redirect(url_for('index'))

@app.route('/display/', methods=['GET'])
def display():
    data = list(db.myposts.find())
    return jsonify({"data": data})

#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
