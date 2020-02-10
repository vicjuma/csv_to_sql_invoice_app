# importing app instance dependency modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initializing my app instance and setting up DB and configuration variables
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invoice.db'
app.secret_key = 'victoroluochjumafrommouseyincorporation'
db = SQLAlchemy(app)




if __name__ == '__main__':
  app.run(debug=True)