from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_bootstrap import Bootstrap


import os
import model

app = Flask(__name__, template_folder='template')
Bootstrap(app)

"""
routes
"""
@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/_predict', methods = ['GET','POST'])
def make_prediction():
    if request.method == 'POST':
        sentence = request.values.get('sentence')
        prediction = model.get_prediction(sentence)
        print(prediction)
        result = {
        'class_name': prediction,
        'sentence': sentence,
        }
        print(result)
        return result



if __name__ == '__main__':
    app.run(debug = True)
