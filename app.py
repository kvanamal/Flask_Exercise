from datetime import date
from time import time
from urllib import request
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.


@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
   global currentDate
   currentDate = datetime.datetime.now()
   return render_template('index.html')
    

@app.get('/calculate')
def displayNumberPage():
    return render_template('form.html')


@app.route('/calculate', methods=['POST'])
def checkNumber():
    global number
    number = request.form['number']
    if not number:
        return 'No number provided.<br><a href="/calculate">Back to home</a>'
    elif number.isalpha():
        return f'{number} is not an integer!<br><a href="/cakculate">Back to home</a>'
    if int(number) % 2 == 0:
        return f'{number} is even.<br><a href="/calculate">Back to home</a>'
    else:
        return f'{number} is odd.<br><a href="/calculate">Back to home</a>'



@app.get('/addStudentOrganisation')
def displayStudentForm():
    return render_template('studentform.html')


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    studentOrg = request.form['org']
    # Append this value to studentOrganisationDetails
    "Student"
    return f'{studentName} is the name and ' + f'{studentOrg} is the org'
    # Display studentDetails.html with all students and organisations
