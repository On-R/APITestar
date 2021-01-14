import json
from flask import Flask, jsonify, url_for, request, render_template, redirect
#import pyodbc as pyodbc
app = Flask(__name__)


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

