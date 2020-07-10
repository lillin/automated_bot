import os

from dotenv import load_dotenv, find_dotenv


env = load_dotenv(find_dotenv())

HOST = os.getenv('HOST', '127.0.0.1') + ':8000'
BASE_URL = f'http://{HOST}/api'

MAX_USERS = int(os.getenv('MAX_USERS', 10))
MAX_POSTS_PER_USER = int(os.getenv('MAX_POSTS_PER_USER', 10))
MAX_LIKES_PER_USER = int(os.getenv('MAX_LIKES_PER_USER', 10))

SIGN_UP_URL = BASE_URL + '/sign_up/'
GET_TOKEN_URL = BASE_URL + '/token/'
POST_URL = BASE_URL + '/post/'
LIKE_URL = BASE_URL + '/post/{post_id}/like/'

BASE_HEADER = {'Content-Type': 'application/json', 'Accept': 'application/json'}
