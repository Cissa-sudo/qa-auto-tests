import random


def random_email():
    return f"user{random.randint(1000,9999)}@test.com"


def random_password():
    return f"pass{random.randint(1000,9999)}"

