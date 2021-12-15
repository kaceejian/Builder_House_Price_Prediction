from flask import Flask, jsonify, render_template, request, redirect, url_for
import pandas as pd 
import json 
import psycopg2
import pickle
import numpy as np
from sklearn.utils import check_array

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################


from sqlalchemy import create_engine
from config import username, password, host, port, database
connection_string = f'{username}:{password}@{host}:{port}/{database}'
engine = create_engine(f'postgresql://{connection_string}')



#Flask Route 
@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/page2")
def page2(): 
    return render_template("page2.html")

@app.route("/page3")
def page3(): 
    return render_template("page3.html")

@app.route("/model", methods=["POST"])
def model():

    RoofMatl = request.form["RoofMatl"]
    if RoofMatl == "":
        RoofMatl = "ClyTile"

    Condition2 = request.form["Condition2"]
    if Condition2 =="":
         Condition2 = "Norm"

    GarageQual = request.form["GarageQual"]
    if GarageQual =="":
         GarageQual = "Ex"

    SaleType = request.form["SaleType"]
    if SaleType =="":
         SaleType = "New"

    Exterior2nd = request.form["Exterior2nd"]
    if Exterior2nd =="":
         Exterior2nd = "Plywood"

    Exterior1st = request.form["Exterior1st"]
    if Exterior1st =="":
         Exterior1st = "Wd Sdng"

    SaleCondition = request.form["SaleCondition"]
    if SaleCondition =="":
         SaleCondition = "Normal"

    RoofStyle = request.form["RoofStyle"]
    if RoofStyle =="":
         RoofStyle = "Gable"

    Functional = request.form["Functional"]
    if Functional =="":
         Functional = "Typ"

    Neighborhood = request.form["Neighborhood"]
    if Neighborhood =="":
         Neighborhood = "Edwards"


    prediction = 0

    # X = 'RoofMatl','Condition2','GarageQual','SaleType','Exterior2nd','Exterior1st','SaleCondition','RoofStyle','Functional','Neighborhood'
    # X = pd.get_dummies

    X = pd.DataFrame(data={"RoofMatl": RoofMatl, 'Condition2': Condition2 ,'GarageQual': GarageQual, 'SaleType': SaleType,'Exterior2nd': Exterior2nd,'Exterior1st': Exterior1st,'SaleCondition': SaleCondition,'RoofStyle': RoofStyle,'Functional': Functional,'Neighborhood': Neighborhood})
    X_dummy = pd.get_dummies(X)


    
   

    filename = 'model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    prediction = loaded_model.predict(X)[0][0]

    prediction = "${0:,.2f}".format(prediction)

    print(prediction)

    return render_template("page3.html", prediction = str(prediction))




@app.route("/prediction")
def prediction():
    df_prediction = pd.read_sql_table(table_name="Prediction", con = engine.connect(), schema ="public")
    df_prediction_json = df_prediction.to_dict(orient="records")
    return jsonify(df_prediction_json)



if __name__ == "__main__":
    app.run(debug=True)
