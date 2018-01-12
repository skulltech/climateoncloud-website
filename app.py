from flask import Flask, request, session, render_template



app = Flask(__name__)
app.secret_key = 'super secret key'


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/charts')
def charts():
	return render_template('charts.html')


if __name__=='__main__':
    app.run()
