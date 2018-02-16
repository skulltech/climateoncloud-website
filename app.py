from flask import Flask, request, session, render_template
import json



app = Flask(__name__)
app.secret_key = 'super secret key'


@app.route('/')
def index():
	with open('cards.json') as f:
		cards = json.load(f)
	return render_template('index.html.clean', cards=cards)


@app.route('/charts')
def charts():
	return render_template('charts.html')


@app.route('/cards')
def cards():
	return render_template('carousel-of-cards.html')


if __name__=='__main__':
    app.run()
