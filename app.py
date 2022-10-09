import os
from flask import Flask
from faker import Faker
import requests
import pandas as pd





fake = Faker()

app = Flask(__name__)




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

