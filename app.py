import os
from flask import Flask
from faker import Faker
import requests
import pandas as pd


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
