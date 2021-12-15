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


# from sqlalchemy import create_engine
# from config import username, password, host, port, database
# connection_string = f'{username}:{password}@{host}:{port}/{database}'
# engine = create_engine(f'postgresql://{connection_string}')



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

# @app.route("/model", methods=["POST"])
# def model():

#     RoofMatl = request.form["RoofMatl"]
#     if RoofMatl == "":
#         RoofMatl = "ClyTile"

#     Condition2 = request.form["Condition2"]
#     if Condition2 =="":
#          Condition2 = "Norm"

#     GarageQual = request.form["GarageQual"]
#     if GarageQual =="":
#          GarageQual = "Ex"

#     SaleType = request.form["SaleType"]
#     if SaleType =="":
#          SaleType = "New"

#     Exterior2nd = request.form["Exterior2nd"]
#     if Exterior2nd =="":
#          Exterior2nd = "Plywood"

#     Exterior1st = request.form["Exterior1st"]
#     if Exterior1st =="":
#          Exterior1st = "Wd Sdng"

#     SaleCondition = request.form["SaleCondition"]
#     if SaleCondition =="":
#          SaleCondition = "Normal"

#     RoofStyle = request.form["RoofStyle"]
#     if RoofStyle =="":
#          RoofStyle = "Gable"

#     Functional = request.form["Functional"]
#     if Functional =="":
#          Functional = "Typ"

#     Neighborhood = request.form["Neighborhood"]
#     if Neighborhood =="":
#          Neighborhood = "Edwards"


#     prediction = 0

#     # X = 'RoofMatl','Condition2','GarageQual','SaleType','Exterior2nd','Exterior1st','SaleCondition','RoofStyle','Functional','Neighborhood'
#     # X = pd.get_dummies

#     X = pd.DataFrame(data={"RoofMatl": RoofMatl, 'Condition2': Condition2 ,'GarageQual': GarageQual, 'SaleType': SaleType,'Exterior2nd': Exterior2nd,'Exterior1st': Exterior1st,'SaleCondition': SaleCondition,'RoofStyle': RoofStyle,'Functional': Functional,'Neighborhood': Neighborhood})
#     X_dummy = pd.get_dummies(X)


    
   

#     filename = 'model.sav'
#     loaded_model = pickle.load(open(filename, 'rb'))

#     prediction = loaded_model.predict(X)[0][0]

#     prediction = "${0:,.2f}".format(prediction)

#     print(prediction)

#     return render_template("page3.html", prediction = str(prediction))

filename = 'model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

@app.route("/model", methods=["POST"])
def model():
     key = [i for i in request.form.keys()]
     value = [i for i in request.form.values()]
     df = pd.DataFrame([value],columns=key)
     df['RoofMatl']=pd.Categorical(df['RoofMatl'],categories=['CompShg', 'WdShngl', 'Metal', 'WdShake', 'Membran', 'Tar&Grv','Roll', 'ClyTile'])
     df['Condition2']=pd.Categorical(df['Condition2'],categories=['Norm', 'Artery', 'RRNn', 'Feedr', 'PosN', 'PosA', 'RRAn', 'RRAe'])
     df['GarageQual']=pd.Categorical(df['GarageQual'],categories=['TA', 'Fa', 'Gd','Ex', 'Po'])
     df['SaleType']=pd.Categorical(df['SaleType'],categories=['WD', 'New', 'COD', 'ConLD', 'ConLI', 'CWD', 'ConLw', 'Con', 'Oth'])
     df['Exterior2nd']=pd.Categorical(df['Exterior2nd'],categories=['VinylSd', 'MetalSd', 'Wd Shng', 'HdBoard', 'Plywood', 'Wd Sdng','CmentBd', 'BrkFace', 'Stucco', 'AsbShng', 'Brk Cmn', 'ImStucc','AsphShn', 'Stone', 'Other', 'CBlock'])
     df['Exterior1st']=pd.Categorical(df['Exterior1st'],categories=['VinylSd', 'MetalSd', 'Wd Sdng', 'HdBoard', 'BrkFace', 'WdShing','CemntBd', 'Plywood', 'AsbShng', 'Stucco', 'BrkComm', 'AsphShn','Stone', 'ImStucc', 'CBlock'])
     df['SaleCondition']=pd.Categorical(df['SaleCondition'],categories=['Normal', 'Abnorml', 'Partial', 'AdjLand', 'Alloca', 'Family'])
     df['RoofStyle']=pd.Categorical(df['RoofStyle'],categories=['Gable', 'Hip', 'Gambrel', 'Mansard', 'Flat', 'Shed'])
     df['Functional']=pd.Categorical(df['Functional'],categories=['Typ', 'Min1', 'Maj1', 'Min2', 'Mod', 'Maj2', 'Sev'])
     df['Neighborhood']=pd.Categorical(df['Neighborhood'],categories=['CollgCr', 'Veenker', 'Crawfor', 'NoRidge', 'Mitchel', 'Somerst','NWAmes', 'OldTown', 'BrkSide', 'Sawyer', 'NridgHt', 'NAmes','SawyerW', 'IDOTRR', 'MeadowV', 'Edwards', 'Timber', 'Gilbert','StoneBr', 'ClearCr', 'NPkVill', 'Blmngtn', 'BrDale', 'SWISU','Blueste'])
     df1= pd.get_dummies(df, columns=['RoofMatl', 'Condition2','GarageQual','SaleType','Exterior2nd','Exterior1st','SaleCondition','RoofStyle','Functional','Neighborhood'])
     dummies_frame = pd.get_dummies(df1)
     df1.reindex(columns = dummies_frame.columns, fill_value=0)

     prediction= loaded_model.predict(df1)

     prediction = "${0:,.2f}".format(prediction)
     print(prediction)

     return render_template("page3.html", prediction = prediction)




@app.route("/prediction")
def prediction():
    df_prediction = pd.read_sql_table(table_name="Prediction", con = engine.connect(), schema ="public")
    df_prediction_json = df_prediction.to_dict(orient="records")
    return jsonify(df_prediction_json)



if __name__ == "__main__":
    app.run(debug=True)
