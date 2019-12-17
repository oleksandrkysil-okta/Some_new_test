import random
from string import ascii_letters


def email_generator(domain_name="@yopmail.com"):
    """
    Creates random email. Contains random 15 characters.
    Using @yopmail.com as default domain name
    """
    name = "".join(random.choice(ascii_letters) for _ in range(15))
    email = name + domain_name
    return email


def name_generator():
    """
     Creates random name. Using 15 random characters.
    """
    name = "".join(random.choice(ascii_letters) for _ in range(15))
    return name


def email_name_generator():
    """
     Returns random email and random name.
    """
    email = email_generator()
    name = name_generator()

    return email, name
