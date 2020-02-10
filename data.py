from flask import Flask
import pandas as pd
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invoice.db'
db = SQLAlchemy(app)

# function to find the monthly totals summary QUIZ1
def monthly_totals():
    jan2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Jan2019 FROM invoices WHERE [*invoicedate] LIKE "%/1/2019"', con=db.engine).to_dict()["Jan2019"][0]

    feb2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Feb2019 FROM invoices WHERE [*invoicedate] LIKE "%/2/2019"', con=db.engine).to_dict()["Feb2019"][0]

    mar2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Mar2019 FROM invoices WHERE [*invoicedate] LIKE "%/3/2019"', con=db.engine).to_dict()["Mar2019"][0]

    apr2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Apr2019 FROM invoices WHERE [*invoicedate] LIKE "%/4/2019"', con=db.engine).to_dict()["Apr2019"][0]

    may2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS May2019 FROM invoices WHERE [*invoicedate] LIKE "%/5/2019"', con=db.engine).to_dict()["May2019"][0]

    jun2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Jun2019 FROM invoices WHERE [*invoicedate] LIKE "%/6/2019"', con=db.engine).to_dict()["Jun2019"][0]

    jul2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Jul2019 FROM invoices WHERE [*invoicedate] LIKE "%/7/2019"', con=db.engine).to_dict()["Jul2019"][0]

    aug2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Aug2019 FROM invoices WHERE [*invoicedate] LIKE "%/8/2019"', con=db.engine).to_dict()["Aug2019"][0]

    sep2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Sep2019 FROM invoices WHERE [*invoicedate] LIKE "%/9/2019"', con=db.engine).to_dict()["Sep2019"][0]

    oct2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Oct2019 FROM invoices WHERE [*invoicedate] LIKE "%/10/2019"', con=db.engine).to_dict()["Oct2019"][0]

    nov2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Nov2019 FROM invoices WHERE [*invoicedate] LIKE "%/11/2019"', con=db.engine).to_dict()["Nov2019"][0]

    dec2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Dec2019 FROM invoices WHERE [*invoicedate] LIKE "%/12/2019"', con=db.engine).to_dict()["Dec2019"][0]

    jan2020 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Jan2020 FROM invoices WHERE [*invoicedate] LIKE "%/1/2020"', con=db.engine).to_dict()["Jan2020"][0]

    feb2020 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Feb2020 FROM invoices WHERE [*invoicedate] LIKE "%/2/2020"', con=db.engine).to_dict()["Feb2020"][0]

    monthly = {
        "first": jan2019,
        "second": feb2019,
        "third": mar2019,
        "forth": apr2019,
        "fifth": may2019,
        "sixth": jun2019,
        "seventh": jul2019,
        "eighth": aug2019,
        "ninth": sep2019,
        "tenth": oct2019,
        "eleventh": nov2019,
        "twelveth": dec2019,
        "thirteenth": jan2020,
        "forteenth": feb2020 
    }
    return monthly


  # top 5 yearly
  def top_customers():
    top2019 = pd.read_sql('SELECT [*contactname], [*quantity] * [*unitamount] AS amount FROM invoices WHERE [*invoicedate] LIKE "%2019" ORDER BY amount DESC LIMIT 5', con=db.engine).to_dict()["*ContactName"]

    top2020 = pd.read_sql('SELECT [*contactname], [*quantity] * [*unitamount] AS amount FROM invoices WHERE [*invoicedate] LIKE "%2020" ORDER BY amount DESC LIMIT 5', con=db.engine).to_dict()["*ContactName"]

    customers = {
        "one": top2019[0],
        "two": top2019[1],
        "three": top2019[2],
        "four": top2019[3],
        "five": top2019[4],
        "six": top2020[0],
        "seven": top2020[1],
        "eight": top2020[2],
        "nine": top2020[3],
        "ten": top2020[4]
    }
    return customers
