# csv_to_sql_invoice_app
Application for accepting csv file upload and saving it to the database for analysis, employing pandas for data analysis and matplotlib for data visualization. SQL is used for querying the database, invoice.db. It uses flask-sqlalchemy orm to set up the database. Through pandaas library, the csv file is read through the read_csv method and converted into a .db file with the pands to_sql. With the .db file, the csv file information can be queried and the data analyzed and visualized trough the use of various plots, specifically lineee graph and barh plot.

# Installation
1. Clone the repo '''using git clone'''
2. Create a virtual environment - use the packages virtualenv which can be installed using the command '''pip install virtualenv''' after which the virtual environment is created with the command virtualenv <Your-environment-name>
  Activate it using source /bin/<Your-environment-name> or . /bin/<Your-environment-name>
3. Run '''pip install -r requirements.txt''' to install all the moodule requirements for the project

# Running
Run the app in the virtual environment using python app.py, open in localhost:5000

# Usage
The frontend has the upload button which only accepts csv files. After uploading the csv file, the data is grabbed, queried and a an invoice.db created, some images are also created inside the working directory using matplotlib and moved to the static folder using the os python built in module. These plots are then displyed from the templates using url_for('static', filename='<filename.png>')
