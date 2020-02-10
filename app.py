# importing app instance dependency modules
from flask import Flask

# initializing my app instance
app = Flask(__name__)




if __name__ == '__main__':
  app.run(debug=True)