from flask import Flask, request,render_template
import datetime
from flask import jsonify

app = Flask(__name__)

mem=[]
@app.route('/home')
def home():
    return "Welcome to Monitor ninja"


@app.route('/process1',methods=['GET','POST'])
def process():
    global mem
    if request.method=='GET':
        print mem
        return mem[-1]
    else:
        data = request.data
        date = str(datetime.datetime.now())
        result = { "data": data, "date":str(date) }
        result= jsonify(result)
        print result
        mem.append(result)
        print mem[-1]
        return result
