import pandas as pd
import pickle
import datetime
from datetime import datetime,date
from elasticsearch import Elasticsearch
from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
"""
IMPORT MODEL MACHINE LEARNING WITH PICKLE
"""
with open("rf_model.pickle", "rb") as file:
    model = pickle.load(file)
"""
SAVE DATA IN ELASTICSEARCH
"""
def save_data(data,quality):
    es = Elasticsearch(
        cloud_id="",
        http_auth=("", ""),
    )
    #INDEX WITH ACTUAL DATE
    created_at = date.today()
    week = created_at.isocalendar()[1]
    year = created_at.isocalendar()[0]
    index='{}{}.{}'.format("wine.",year,week)
    data.update({'quality': quality[0]})
    updict = {'wine':index}
    data = {**updict, **data}
    res = es.index(index=index, body=data)

"""
API REST
"""
app = Flask(__name__)
@app.route('/model', methods=['POST'])
def post():

    data = request.get_json(force=True)
    fixed_acidity = str(data["fixed acidity"])
    volatile_acidity = str(data["volatile acidity"])
    citric_acid = str(data["citric acid"])
    chlorides = str(data["chlorides"])
    free_sulfur_dioxide = str(data["free sulfur dioxide"])
    total_sulfur_dioxide = str(data["total sulfur dioxide"])
    free_sulfur_dioxide = str(data["free sulfur dioxide"])
    total_sulfur_dioxide = str(data["total sulfur dioxide"])
    ph = str(data["ph"])
    sulphates = str(data["sulphates"])
    alcohol = str(data["alcohol"])
    allData = [fixed_acidity, volatile_acidity, citric_acid, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, free_sulfur_dioxide, total_sulfur_dioxide, ph, sulphates, alcohol]
    columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']

    df = pd.DataFrame(data=[allData], columns=columns)
    quality = model.predict(df)

    #SAVE THE DATA AND QUALITY PREDICTED IN ELASTICSEARCH
    if len(data) != 0:
        save_data(data,quality)
    else:
        print("error: No data")

    if quality <= 3:
        json = {"quality": "Low Quality", "value": quality[0]}
    elif quality > 4 and quality <7:
        json = {"quality": "Medium Quality", "value": quality[0]}
    else:
        json = {"quality": "High Quality", "value": quality[0]}

    return jsonify(json)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=False)
