# importing app instance dependency modules
from flask import Flask, request, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import matplotlib.pyplot as plt
import os
from data import monthly_totals, top_customers, general_top_five


# initializing my app instance and setting up DB and configuration variables
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invoice.db'
app.secret_key = 'victoroluochjumafrommouseyincorporation'
db = SQLAlchemy(app)

ALLOWED_EXTENSIONS = set(['csv'])

current_dir = os.getcwd()
src = current_dir
dest = os.path.join(current_dir, "static")


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

    # grahical plots
    days30 = pd.read_sql('SELECT SUM([*quantity] * [*unitamount]) AS total, * FROM invoices WHERE [*InvoiceDate] BETWEEN "1/11/2019" AND "29/11/2019" GROUP BY [*InvoiceDate]', con=db.engine).to_dict()["total"]

    day0 = days30[0]
    day1 = days30[1] + day0
    day2 = days30[2] + day1
    day3 = days30[3] + day2
    day4 = days30[4] + day3
    day5 = days30[5] + day4
    day6 = days30[6] + day5
    day7 = days30[7] + day6

    barC = pd.read_sql('SELECT [*contactname], [*quantity] * [*unitamount] AS amount FROM invoices ORDER BY amount DESC LIMIT 5', con=db.engine).to_dict()["*ContactName"]

    barA = pd.read_sql('SELECT [*contactname], [*quantity] * [*unitamount] AS amount FROM invoices ORDER BY amount DESC LIMIT 5', con=db.engine).to_dict()["amount"]

    y0 = barC[0]
    y1 = barC[1]
    y2 = barC[2]
    y3 = barC[3]
    y4 = barC[4]

    x0 = barA[0]
    x1 = barA[1]
    x2 = barA[2]
    x3 = barA[3]
    x4 = barA[4]

    plt.style.use("seaborn")
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle("GRAPHICAL PRESENTATIONS")
    ax1.plot(["Nov7","Nov10","Nov14","Nov15","Nov19","Nov20","Nov24","Nov29"],[day0,day1,day2,day3,day4,day5,day6,day7], color='blue')

    ax2.barh([y4,y3,y2,y1,y0], [x4,x3,x2,x1,x0], color="blue")

    plt.savefig('graphs.png')

    if not os.path.isfile(dest + '/graphs.png'):
        os.rename(src + "/graphs.png", dest + "/graphs.png")

    return render_template('data.html', monthly_totals=monthly_totals(), customers=top_customers(), general=general_top_five())





if __name__ == '__main__':
  app.run(debug=True)