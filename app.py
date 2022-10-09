import os
from flask import Flask
from faker import Faker
import requests

fake = Faker()

app = Flask(__name__)


@app.route('/')
def red_method():
    pass


def user_data_method():
    pass


def red_csv_method():
    pass


def astros_method():
    """
    Function make a request to the URL and create html
    templates with astronaut list
    """
    url = 'http://api.open-notify.org/astros.json'
    responseJSON = requests.get(url).json()
    astros = """
        <h1>List astronauts</h1>
        <h2>There are {astronauts_count} astronauts in orbit</h2>
        <ul>
            {astronauts_list}
        </ul>
        <a href="/">Back</a>
        """
    astronauts_list = ''
    for astronaut in responseJSON.get('people'):
        astronauts_list += "<li>{astronaut_name}</li>".format(
                            astronaut_name=astronaut.get("name"),
                            )
    return astros.format(
        astronauts_list=astronauts_list,
        astronauts_count=responseJSON.get('number'))
