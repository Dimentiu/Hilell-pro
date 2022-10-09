import os
from flask import Flask
from faker import Faker

fake = Faker()

app = Flask(__name__)


@app.route('/')
def red_method():
    """Function red txt file
    """
    red_path = os.path.join(os.getcwd(), "requirements.txt")
    with open(red_path) as f:
        data = f.readlines()
        return data


def user_data_method():
    pass


def red_csv_method():
    pass


def astros_method():
    pass