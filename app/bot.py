import random
import requests

from app import settings
from app.generators import (
    generate_users_payload,
    generate_post_payload
)


class Bot:
    def __init__(self):
        self.authorized_headers = list()
        self.posts_ids = list()

    def __call__(self, *args, **kwargs):
        self.sign_up_users()

        # TODO: change to "all posts are created, then all users do their job" !
        for header in self.authorized_headers:
            self.create_posts(header)
            self.like_post(header)

    def sign_up_users(self):
        # get fake credentials for "users"
        payloads = [generate_users_payload() for _ in range(settings.MAX_USERS)]

        # sign up every user
        for payload in payloads:
            requests.post(
                settings.SIGN_UP_URL, json=payload, headers=settings.BASE_HEADER
            )

        # exchange credentials to tokens
        for payload in payloads:
            credentials = dict((k, v) for k, v in payload.items() if k in ['username', 'password'])

            response = requests.post(
                settings.GET_TOKEN_URL, json=credentials, headers=settings.BASE_HEADER
            ).json()

            authorized_header = settings.BASE_HEADER.copy()
            authorized_header['Authorization'] = f'Bearer {response["access"]}'
            self.authorized_headers.append(authorized_header)

    def create_posts(self, header):
        # every user creates posts from range to max given number
        posts_amount = range(random.randrange(1, settings.MAX_POSTS_PER_USER))

        # TODO: investigate KeyError 'id' issue on second iter 
        self.posts_ids += \
            [
                requests.post(
                    settings.POST_URL, json=generate_post_payload(), headers=header
                ).json()['id'] for _ in posts_amount
            ]

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

        for _ in likes_amount:
            for url in urls_to_posts:
                requests.post(url, headers=header)
