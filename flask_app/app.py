import logging

from flask import Flask
from flask import jsonify
from prometheus_flask_exporter import PrometheusMetrics


logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to INFO")

api = Flask(__name__)
metrics = PrometheusMetrics(api)

metrics.info(
    "app_info", "Just an App", version="1.0.0")

@api.route("/simple/")
def hello():
    return jsonify(say_hello())

def say_hello():
    return {"message": "hello"}

