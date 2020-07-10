"""
Just initialize instance and run application.
"""
import logging
import requests

from app import settings
from app.bot import Bot


logging.basicConfig(level=logging.INFO)


message = 'Checking host... {}'

try:
    requests.get(settings.BASE_URL)
    logging.info(message.format('OK'))
except requests.exceptions.ConnectionError:
    logging.info(message.format('FAILED'))
    logging.error(f'Connection failed for {settings.BASE_URL}, please provide other host name.')
else:
    Bot()()
