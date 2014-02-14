
import re
from flask import Flask, jsonify, request, render_template, json
app = Flask(__name__, static_folder='static', template_folder= 'templates')

app.secret_key= '\ybf\xb10\x94au\x2f\xf9\se2\x3f\x93\x26(\xdf\xe4\xaf\x1f\x86k\xb3\x2fQ%1'


@app.route('/')
def index():
	
	return render_template('home.html')



if __name__ == '__main__':
	app.run(debug=True)

