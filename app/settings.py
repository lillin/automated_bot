import os


# TODO: get public ipv4 through service api + investigate issue with localhost
BASE_URL = f'http://192.168.98.161:8000/api'

MAX_USERS = int(os.environ.get('max_users'))
MAX_POSTS_PER_USER = int(os.environ.get('max_posts_per_user'))
MAX_LIKES_PER_USER = int(os.environ.get('max_like_per_user'))

SIGN_UP_URL = BASE_URL + '/sign_up/'
GET_TOKEN_URL = BASE_URL + '/token/'
POST_URL = BASE_URL + '/post/'
LIKE_URL = BASE_URL + '/post/{post_id}/like/'

BASE_HEADER = {'Content-Type': 'application/json', 'Accept': 'application/json'}
