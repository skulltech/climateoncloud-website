import scraper
import os
import json
from flask import Flask, request, session, render_template



app = Flask(__name__)
app.secret_key = 'super secret key'


@app.route('/rainfall')
def rainfall(name):
    if not os.path.exists(os.path.join('data', 'rainfall.json')):
    	scraper.rainfall()

    with open(os.path.join('data', 'rainfall.json')) as file:
    	data = json.load(file)
    


@app.route('/inside')
def inside():
    return render_template('inside.html')


if __name__=='__main__':
    app.run()
