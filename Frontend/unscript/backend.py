import numpy as np
from flask import Flask, render_template, request, flash, redirect
from flask_mysqldb import MySQL, MySQLdb
#from flask_sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy
import mysql
import json
import subprocess
import sys
import PyXGBoost
import xgboost
import mysql.connector
import pickle
import numpy as np
from werkzeug.utils import secure_filename
import os
# import magic
import urllib.request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cairocoders-ednalan'
model = pickle.load(open('xgboostfinal.pkl','rb'))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Yashw@123@localhost:3306/deepblue'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Yashw@123'
app.config['MYSQL_DB'] = 'unscript'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
# db = SQLAlchemy(app)

#transid= "C1282434920"



@app.route('/', methods=["POST", "GET"])
#def hello():
 #   return render_template('mainpage.html')



@app.route("/upload", methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        transid = request.form.get('tid')
        result=cur.execute('SELECT * FROM smalldb WHERE nameOrig=%s', (transid,))
        if result>0:
            row = cur.fetchall()
            for i in row:
                con_dic=i

            val = (con_dic.get("step"))
            val1 = (con_dic.get("type"))
            val2 = (con_dic.get("amount"))
            val3 = (con_dic.get("nameOrig"))
            val4 = (con_dic.get("oldbalanceOrg"))
            val5 = (con_dic.get("newbalanceOrig"))
            val6 = (con_dic.get("nameDest"))
            val7 = (con_dic.get("oldbalanceDest"))
            val8 = (con_dic.get("newbalanceDest"))
            val9 = (con_dic.get("isFraud"))
            val10 = (con_dic.get("errorBalanceOrg"))
            val11= (con_dic.get("errorBalanceDest"))
            val12= (con_dic.get("HourOfDay"))

            final_list=[val,val2,val4,val5,val7,val8,val10,val11,val12]
            final_array=[np.array(final_list)]



            prediction=model.predict(final_array)
            print(prediction)

            if val9==0 :
                fin_res= "Not fraudulent"
            else:
                fin_res="fraudulent"
            if val7==0 and val8==0 :
                old_amount= "Merchant"
                new_amount = "Merchant"
            else:
                old_amount = val7
                new_amount = val8
            print(prediction[0])
            if prediction[0] == 1 :
                res="fraudulent"
            else:
                res=" Not fraudulent"








            return render_template('secondpage.html',val=val,val1=val1, val2=val2 , val3=val3, val4=val4,val5=val5,val6=val6,val7=old_amount,val8=new_amount, val9=fin_res,val12=val12,val13=res)
            return redirect('/second')


    return render_template('mainpage.html')


@app.route('/second')
def second():
    return render_template('secondpage.html')








if __name__ == "__main__":
  app.run(debug=True)

#app.run(debug=True)
