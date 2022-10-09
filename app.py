import os
from flask import Flask
from faker import Faker

fake = Faker()

app = Flask(__name__)


@app.route('/')
def red_method():
    pass


def user_data_method():
    """Function generate 100 random users"""
    for i in range(101):
        name = fake.name()
        email = fake.email()
        response = {
            "name": name,
            "email": email
        }
    return (response)


def red_csv_method():
    pass


def astros_method():
    pass