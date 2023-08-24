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
    first_name = requests.get('first')
    last_name = requests.get('last')

    return render_template('thank_you.html',first=first_name,last=last_name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html')

if __name__=="__main__":
    app.run(debug=True)
    