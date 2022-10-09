import os
from flask import Flask
from faker import Faker

fake = Faker()

app = Flask(__name__)


@app.route('/')
def red_method():
    pass

def user_data_method():
    pass


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
    pass