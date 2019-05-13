from flask import Flask, request
import lightf
app = Flask(__name__)

@app.route('/query_example')
def query_example():
    object1=request.args.get('object')
    action1=request.args.get('action')
    if (action1 == 'on'):
        lightf.lightON()
    else:
        lightf.lightOFF()

