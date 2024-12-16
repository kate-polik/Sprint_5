import random
import string
import secrets


def generate_email():
    first_name = "test"
    last_name = "user"
    random_digits = ''.join(random.choices(string.digits, k=10))
    domain = "yandex.ru"
    return f"{first_name}{last_name}{random_digits}@{domain}"


def generate_password(length=8):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(alphabet) for _ in range(length))


class DataInput:
    email = generate_email()
    password = generate_password(8)
