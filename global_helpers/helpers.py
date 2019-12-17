import random
from string import ascii_letters


def generate_random_string(length=15):
    """
    Generate random string with given length.
    Default length 15 characters
    """
    return "".join(random.choice(ascii_letters) for _ in range(length))


def email_generator(name_length=15, domain_name="@yopmail.com"):
    """
    Creates random email. Contains random 15 characters.
    Using @yopmail.com as default domain name
    """
    name = generate_random_string(name_length)
    email = name + domain_name
    return email


def name_generator(name_length=15):
    """
     Creates random name. Using 15 random characters.
    """
    name = generate_random_string(name_length)
    return name


def email_name_generator():
    """
     Returns random email and random name.
    """
    email = email_generator()
    name = name_generator()

    return email, name
