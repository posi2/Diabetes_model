from flask import Flask, render_template
from keras import backend as K

from flask import *
from model import prediction

app=Flask(__name__,template_folder='template')
K.clear_session()
@app.route('/')
def index():
    return render_template('layout.html')
    #request.method and request.form
    #nmpy_list from form
    #output = model(nmpy_list)


@app.route('/',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result=request.form
        output = prediction(result)
        del result
        return render_template("result.html")



if __name__ == '__main__' :
    app.run(debug = True)
