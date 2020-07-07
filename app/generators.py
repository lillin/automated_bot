import random
import string


def generate_users_payload():
    """
    Generate username, email, password for sign up and token auth.
    :return:
    """

    username = generate_string(length=8)
    email = generate_string(length=8, for_type='email')
    password = generate_string(length=8)

    return {"username": username, "email": email, "password": password}


def generate_post_payload():
    """
    Generate title and body for blog post.
    :return:
    """

    title = generate_string(random.randrange(20))
    body = generate_string(random.randrange(10), for_type='post')

    return {'title': title, 'body': body}


def generate_string(length: int, for_type=None) -> str:
    """
    Helper function to generate strings for different purposes.
    :param length:
    :param for_type:
    :return: str
    """

    available_types = ['email', 'post', ]
    if for_type:
        assert for_type in available_types, 'Unknown requested type for string to generate.'

    pattern = ''.join((random.choice(string.ascii_lowercase) for _ in range(length)))

    if for_type == 'email':
        return pattern + '@' + 'address.com'
    if for_type == 'post':
        return (pattern + ' ') * 150

    return pattern
