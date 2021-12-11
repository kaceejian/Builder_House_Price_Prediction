from flask import Flask, jsonify, render_template, request, redirect, url_for
import pandas as pd 
import json 
import psycopg2

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

@app.route("/prediction")
def prediction():
    df_prediction = pd.read_sql_table(table_name="Prediction", con = engine.connect(), schema ="public")
    df_prediction_json = df_prediction.to_dict(orient="records")
    return jsonify(df_prediction_json)


if __name__ == "__main__":
    app.run(debug=True)
