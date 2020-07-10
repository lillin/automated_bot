import logging
import random
import requests

from app import settings
from app.generators import (
    generate_users_payload,
    generate_post_payload
)


class Bot:
    def __init__(self):
        self.users_payload = [generate_users_payload() for _ in range(settings.MAX_USERS)]
        self.authorized_headers = list()
        self.posts_ids = list()

    def __call__(self, *args, **kwargs):
        self.sign_up_users()
        self.obtain_tokens()

        for header in self.authorized_headers:
            self.create_posts(header)

        for header in self.authorized_headers:
            self.like_post(header)

    def sign_up_users(self):
        # sign up every user

        logging.info('Sign up users...')
        for payload in self.users_payload:
            requests.post(
                settings.SIGN_UP_URL, json=payload, headers=settings.BASE_HEADER
            )

    def obtain_tokens(self):
        # exchange credentials to tokens

        logging.info('Obtaining users\' tokens...')
        for payload in self.users_payload:
            credentials = dict((k, v) for k, v in payload.items() if k in ['username', 'password'])

            response = requests.post(
                settings.GET_TOKEN_URL, json=credentials, headers=settings.BASE_HEADER
            ).json()

            header = settings.BASE_HEADER.copy()
            header['Authorization'] = f'Bearer {response["access"]}'
            self.authorized_headers.append(header)

    def create_posts(self, header):
        # every user creates posts from range to max given number
        posts_amount = range(random.randrange(1, settings.MAX_POSTS_PER_USER))

        posts_ids = [
            requests.post(
                settings.POST_URL, json=generate_post_payload(), headers=header
            ).json()['id'] for _ in posts_amount
        ]

        logging.info(f'User adding posts {posts_ids}')
        self.posts_ids += posts_ids

    def like_post(self, header):
        # amount of likes for 1 user (equal to amount of posts user can create)
        max_available_likes_amount = \
            settings.MAX_LIKES_PER_USER \
            if settings.MAX_LIKES_PER_USER <= len(self.posts_ids) \
            else len(self.posts_ids)

        likes_amount = range(random.randrange(1, max_available_likes_amount))

        # random posts' ids (amount based on amount of available likes)
        posts_choices = [random.choice(self.posts_ids) for _ in likes_amount]

        urls_to_posts = [settings.LIKE_URL.format(post_id=i) for i in posts_choices]

        for url in urls_to_posts:
            logging.info(f'Like post on {url}')
            requests.post(url, headers=header)
