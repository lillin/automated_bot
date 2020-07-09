import os

import netifaces as ni
from dotenv import load_dotenv, find_dotenv


env = load_dotenv(find_dotenv())


def get_ip():
    """
    Get IPv4 address of ethernet interface of machine.
    """
    return ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']


HOST = os.getenv('HOST', get_ip()) + ':8000'
BASE_URL = f'http://{HOST}/api'

MAX_USERS = int(os.getenv('MAX_USERS', 10))
MAX_POSTS_PER_USER = int(os.getenv('MAX_POSTS_PER_USER', 10))
MAX_LIKES_PER_USER = int(os.getenv('MAX_LIKES_PER_USER', 10))

SIGN_UP_URL = BASE_URL + '/sign_up/'
GET_TOKEN_URL = BASE_URL + '/token/'
POST_URL = BASE_URL + '/post/'
LIKE_URL = BASE_URL + '/post/{post_id}/like/'

BASE_HEADER = {'Content-Type': 'application/json', 'Accept': 'application/json'}
