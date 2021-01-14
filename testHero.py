
from flask import Flask
import matplotlib.pyplot as plt
import pyodbc as pyodbc
import pandas as pd
import sqlite3
from flask import Flask, jsonify, url_for, request, render_template, redirect
import pyodbc as pyodbc
import numpy as np
app = Flask(__name__)

#with open(r"C:\Users\Admin\Desktop\customers.json") as f:
import json
with open('customers.json') as f:
    customers = json.load(f)


@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        kundnummer = request.form["kundid"]
        return redirect(url_for("get_customer", Id=kundnummer))  

    else: 
        return render_template('home.html') 

@app.route('/api/v1/customers', methods =["GET"])
def get_customers():
    return jsonify({"customers":customers})


@app.route('/api/v1/customers/<int:Id>', methods =["GET"])
def get_customer(Id):
    customer = [ customer for customer in customers if customer ['Id'] == Id ]
    return jsonify({"customers":customer})


if __name__ == '__main__':
    app.run()

