import socket
import os


def get_ip():
    # TODO: get IPv4 for WiFi adapter
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('10.255.255.255', 1))
    return '192.168.0.175' + ':8000'


HOST = os.environ.get('host', get_ip())
BASE_URL = f'http://{HOST}/api'

MAX_USERS = int(os.environ.get('max_users'))
MAX_POSTS_PER_USER = int(os.environ.get('max_posts_per_user'))
MAX_LIKES_PER_USER = int(os.environ.get('max_like_per_user'))

SIGN_UP_URL = BASE_URL + '/sign_up/'
GET_TOKEN_URL = BASE_URL + '/token/'
POST_URL = BASE_URL + '/post/'
LIKE_URL = BASE_URL + '/post/{post_id}/like/'

BASE_HEADER = {'Content-Type': 'application/json', 'Accept': 'application/json'}
