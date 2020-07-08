import random
import string


def generate_users_payload():
    """
    Generate username, email, password for sign up and token auth.
    """

    username = generate_string(length=8)
    email = generate_string(length=8, email=True)
    password = generate_string(length=8)

    return {"username": username, "email": email, "password": password}


def generate_post_payload():
    """
    Generate title and body for blog post.
    """

    title = generate_string(length=random.randrange(2, 20))
    body = generate_string(length=random.randrange(2, 20), post=True)

    return {'title': title, 'body': body}


def generate_string(length: int, email=False, post=False) -> str:
    """
    Helper function to generate strings for different purposes.
    :param post: True to generate strings for post
    :param email: True to generate email
    :param length: Desirable length of string
    """

    pattern = ''.join((random.choice(string.digits + string.ascii_letters) for _ in range(length)))

    if email:
        return pattern + '@' + 'address.com'
    if post:
        return (pattern + ' ') * 150

    return pattern
