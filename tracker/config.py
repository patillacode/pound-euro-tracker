import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CURRENCY_API_ENDPOINT = 'http://api.fixer.io'
CURRENCY_BASE = 'GBP'
CURRENCY_SYMBOL = 'EUR'

DATABASE_PATH = '{}/tracker/db/currency.json'.format(BASE_DIR)
