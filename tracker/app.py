import traceback

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

from currency import get_currency_data
from currency import populate_data

application = Flask(__name__)


# redirect all non existing urls to index.html
@application.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


@application.route('/', methods=['GET'])
def index():
    try:
        data = get_currency_data()
        return render_template('index.html', data=data)
        # return render_template('index.html', request=request)
    except:
        application.logger.error(traceback.format_exc())
        return render_template('404.html', request=request)


@application.route('/populate/<from_date>/', methods=['GET'])
def populate(from_date):
    try:
        return jsonify(populate_data(from_date)), 200
    except:
        application.logger.error(traceback.format_exc())
        return render_template('404.html', request=request)
