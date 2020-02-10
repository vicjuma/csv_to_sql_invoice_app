# importing app instance dependency modules
from flask import Flask, request, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import os
from data import monthly_totals, top_customers

# initializing my app instance and setting up DB and configuration variables
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invoice.db'
app.secret_key = 'victoroluochjumafrommouseyincorporation'
db = SQLAlchemy(app)

ALLOWED_EXTENSIONS = set(['csv'])


# form get route
@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')


# file post route
@app.route('/data', methods=["POST"])
def transform_view():
    if request.method == 'POST':
        f = request.files['data_file']
        df = pd.read_csv(f, parse_dates=True, usecols=[0, 10, 12, 13, 16, 17, 18], encoding='UTF-16 LE')
        df.to_sql('invoices', con=db.engine, index=False, index_label='id', if_exists='replace')
        return render_template('data.html', monthly_totals=monthly_totals(), customers=top_customers())
    return 'Oops, Try again something went wrong!'





if __name__ == '__main__':
  app.run(debug=True)