from flask import Flask, render_template, request, flash, redirect
from flask_mysqldb import MySQL, MySQLdb
#from flask_sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy
import mysql
import json
import subprocess
import sys
import mysql.connector
from werkzeug.utils import secure_filename
import os
# import magic
import urllib.request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cairocoders-ednalan'

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
        result=cur.execute('SELECT * FROM db WHERE nameOrig=%s', (transid,))
        if result>0:
            row = cur.fetchall()
            for i in row:
                con_dic=i
            val1 = (con_dic.get("MyUnknownColumn"))
            val2 = (con_dic.get("Unnamed"))
            val3 = (con_dic.get("step"))
            val4 = (con_dic.get("type"))
            val5 = (con_dic.get("amount"))
            val6 = (con_dic.get("nameOrig"))
            val7 = (con_dic.get("oldbalanceOrg"))
            val8 = (con_dic.get("newbalanceOrig"))
            val9 = (con_dic.get("nameDest"))
            val10 = (con_dic.get("isFraud"))
            val11 = (con_dic.get("oldbalanceDest"))
            val12 = (con_dic.get("newbalanceDest"))

            if val10==0 :
                fin_res= "Not fraudulent"
            else:
                fin_res="fraudulent"
            if val11==0 :
                old_amount= "Merchant"
            else:
                old_amount = val11
            if val12== 0:
                val12="Merchant"
            else:
                new_amount=val12






            return render_template('secondpage.html',val1=val1, val2=val2 , val3=val3, val4=val4,val5=val5,val6=val6,val7=val7,val8=val8, val9=val9,val10=fin_res, old_amount=old_amount,new_amount=new_amount)
            return redirect('/second')


    return render_template('mainpage.html')


@app.route('/second')
def second():
    return render_template('secondpage.html')








if __name__ == "__main__":
  app.run(debug=True)

#app.run(debug=True)
