import random

from faker import Faker


def create_user():
    fake = Faker("ru_RU")
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
    }


def create_product():
    number_product = str(random.randint(100, 200))
    return {
        "product_name": "product" + number_product,
        "meta_tag_title": "product" + number_product,
        "model": "model" + number_product,
        "seo": "product" + "-" + number_product,
    }
