from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from wineQuality.pipeline import PredictionPipeline
from wineQuality import logger
app = Flask(__name__)


@app.route('/train', methods=['GET'])
def training():
    os.system('python main.py')
    return 'Training Successful'

@app.route('/', methods=['GET'])
def homePage():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            fixed_acidity =float(request.form['fixed-acidity'])
            volatile_acidity =float(request.form['volatile-acidity'])
            citric_acid =float(request.form['citric-acid'])
            residual_sugar =float(request.form['residual-sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free-sulfur-dioxide'])
            total_sulfur_dioxide =float(request.form['total-sulfur-dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
            
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1, 11)
            logger.info(f'data: {data}')
            obj = PredictionPipeline()
            predict = obj.prediction(data)

            return render_template('index.html', prediction_text = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)