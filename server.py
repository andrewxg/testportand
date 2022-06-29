from lib2to3.pgen2.token import NEWLINE
from flask import Flask, render_template, request
from datetime import datetime
import csv

hr = '---------------------------------------------'
now = datetime.now()
dt = now.strftime("%B %d, %Y - %H:%M %p")

app = Flask(__name__)

print(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/home')
def pages():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/work')
def work():
    return render_template('work.html')

def write_to_db_txt(data):
    with open('database.txt', 'a') as dbt:
        dbt.write(f"EMAIL : {data['email_id']}\nSUBJECT : {data['subject']}\nMESSAGE : {data['message']}\nDATE - TIME : {dt}\n{hr}\n")

def write_to_db_csv(data):
    with open('database.csv', 'a', newline='') as dbc:
        csv_write = csv.writer(dbc, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([data['email_id'],data['subject'],data['message'],dt])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_db_csv(data)
        return 'Form Subbmitted !'
    else:
        return 'Error Occured !'
    













# @app.route('/components')
# def components():
#     return render_template('components.html')

# # dynamic
# @app.route('/<string:pagename>')
# def pages(pagename):
#     return render_template(pagename)