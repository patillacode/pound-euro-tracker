import datetime
import requests
import time
# import traceback

from flask import current_app
from tinydb import Query
from tinydb import TinyDB

import config


def get_currency_data():
    # select database/table
    db = TinyDB(config.DATABASE_PATH)
    rates = db.table('rates')

    dates = []
    values = []

    for data in rates.all():
        dates.append(data['date'])
        values.append(data['rates'][config.CURRENCY_SYMBOL])

    return {'values': values,
            'dates': dates,
            'currency_base': config.CURRENCY_BASE,
            'currency_symbol': config.CURRENCY_SYMBOL}


def get_rates_from_api(date):
    data = requests.get('{}/{}?base={}&symbols={}'.format(
        config.CURRENCY_API_ENDPOINT,
        date,
        config.CURRENCY_BASE,
        config.CURRENCY_SYMBOL))
    if data.status_code == 429:
        current_app.logger.debug('Rate limit exceeded, waiting 5 secs...')
        time.sleep(5)
        return get_rates_from_api(date)
    elif data.status_code == 200:
        return data
    else:
        raise


def populate_data(from_date):
    current_app.logger.debug('Populating db with data since {}'.format(
        from_date))
    # select database/table
    db = TinyDB(config.DATABASE_PATH)
    rates = db.table('rates')
    query = Query()

    today = datetime.datetime.today()
    today_date = '{}-{}-{}'.format(today.year, today.month, today.day)

    start_date = datetime.datetime.strptime(from_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(today_date, '%Y-%m-%d')

    current_app.logger.debug('Gathering data from {} ...'.format(
        config.CURRENCY_API_ENDPOINT))

    if start_date <= end_date:
        for n in range((end_date - start_date).days + 1):
            date = (start_date + datetime.timedelta(n)).strftime("%Y-%m-%d")
            print 'date: {}'.format(date)
            # check if we already have data for given date
            # if so, skip, if not, insert.
            if len(rates.search(query.date == date)):
                current_app.logger.debug('Already have data for given date. '
                                         'Skipping...')
            else:
                # gather data from 3rd party
                data = get_rates_from_api(date)
                print 'Setting data[date] from {} to {}'.format(data.json()['date'], date)
                data = data.json()
                data['date'] = date
                print data
                rates.insert(data)

    return {'status': True}
