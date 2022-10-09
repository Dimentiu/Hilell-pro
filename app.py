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
    """Function read *.csv file and finds the average value each column"""
    df = pd.read_csv('hw.csv', sep=',')
    header_list = df.columns.tolist()
    header_list.pop(0)
    height = "Height"
    weight = "Weight"
    average_param = ""
    average_table = """
            <h1>Average Data</h1>
            <table>
                {average_param}
            </table>
            <a href="/">Back</a>
        """
    for column_name in header_list:
        if height in column_name:
            average_param += """
                <tr>
                    {height} (Cm)</td>
                    {height_data}</td>
                </tr>
            """.format(
                height=height,
                height_data=round(df[column_name].mean()*2.54, 2),
                )
        else:
            average_param = average_param + """
                <tr>
                    {weight} (Kg)</td>
                    {weight_data}</td>
                </tr>
            """.format(
                weight=weight,
                weight_data=round(df[column_name].mean()*0.453592, 2),
                )
    return average_table.format(
        average_param=average_param)


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
