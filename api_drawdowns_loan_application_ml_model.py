import datetime
import logging
import os

from flask import Flask, request
from flask_cors import CORS

from service_api_drawdowns.drawdown_service_api import get_pred

application = Flask(__name__)


@application.route('/', methods=['GET'])
def hello():
    return "hello"


@application.route('/drawdowns_loan_decision_ml_model/v1/invoice_id/<invoice_id>', methods=['GET'])
def loan_decision_ml_model(invoice_id):
    return get_pred(invoice_id)

CORS(application)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
