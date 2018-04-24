from flask import Flask, request,render_template
import datetime
from flask import jsonify

app = Flask(__name__)

@app.route('/home')
def home():
    return "Welcome to Monitor ninja"


@app.route('/process1',methods=['GET','POST'])
def process():
    data = request.data
    date = str(datetime.datetime.now())
    result = { "data": data, "date":str(date) }
    result= jsonify(result)
    return render_template('process.html', name=result)
