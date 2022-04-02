import os
import sys
import json
import uuid
import flask
import base64

from flask_cors import CORS
from flask import Flask, redirect, request

from src.tools import Tools
from src.database import Database

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*", "Access-Control-Allow-Origin" : "*"}})
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_FILE_DIR'] = './.flask_session/'
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

tools = Tools()
database = Database()

@app.route("/api/version", methods = [ "GET" ])
def version():
    status = tools.status.builder(tools.status.SUCCESS, { "version" : "0.0.1", "developer" : True })

    return (status)

@app.route("/api/upload", methods = [ "POST" ])
def upload():
    ip = flask.request.remote_addr
    body = flask.request.json

    return (database.upload(body["image"], ip))

@app.route("/api/search/<id>", methods = [ "GET" ])
def search(id):
    return (database.search(id))

@app.route("/api/count", methods = [ "GET" ])
def counter():
    return (database.counter())

@app.route("/api", methods = [ "GET" ])
def root():
    status = tools.status.builder(tools.status.SUCCESS, "welcome")

    return (status)

if (__name__ == "__main__"):
    app.run(threaded = True, host = "0.0.0.0", port = 8080, debug = True)
