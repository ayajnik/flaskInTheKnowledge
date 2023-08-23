from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/thank_you')
def thank_you():
    first = requests.args.get('first')
    last = requests.args.get('last')

    return render_template('thank_you.html',first=first,last=last)
    