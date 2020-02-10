# importing app instance dependency modules
from flask import Flask, request, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import os

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
@app.route('/data', methods=["POST", "GET"])
def transform_view():
    f = request.files['file']
    if request.method == 'POST':
        f.seek(0, os.SEEK_END)
        if f.tell() == 0:
            flash('No file selected')
            return redirect(request.url)
        if f:
            df = pd.read_csv(f, parse_dates=True, usecols=[0, 10, 12, 13, 16, 17, 18], encoding='UTF-16 LE')
            df.to_sql('invoices', con=db.engine, index=False, index_label='id', if_exists='replace')
            return df.to_dict()
    return 'Use the POST verb'




if __name__ == '__main__':
  app.run(debug=True)