import os
import re
import shutil
import csv
import sys
import pyodbc
from io import BytesIO
# from turtle import title, width
from flask import Flask,render_template, url_for, flash, redirect, request
# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileRequired, FileAllowed
# from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_bootstrap import Bootstrap
# from wtforms import StringField, IntegerField, SubmitField, SelectField
# from wtforms.validators import DataRequired
from PIL import Image

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = '0626fuyi'
server = 'notminusone.database.windows.net'
database = 'notminusoneDatabase'
username = 'not-1'
password = '0626Fuyi' 
driver= '{ODBC Driver 17 for SQL Server}'
# 
# ROUTES!


@app.route('/',methods=["GET","POST"])
def part10():
	if request.method=='GET':
		return render_template('part10.html',part10_active="active",title="Part 10")
	if request.method=='POST':
		low=int(request.form["Low"])
		high=int(request.form["High"])
		if(low>high):
			a=low
			low=high
			high=a
		if low>0 and high>0:
			cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:notminusone.database.windows.net,1433;Database=notminusoneDatabase;Uid=not-1;Pwd={0626Fuyi};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
			cursor = cnxn.cursor()
			cursor.execute("select sum(num),food from f where store>=? and store<=? group by food",low,high)
			a = cursor.fetchall()
			count=[]
			name=[]
			for item in a:
				count.append(item[0])
				name.append(item[1])
			dic={}
			dic['count']=count
			dic['name']=name
			dataJson=json.dumps(dic,ensure_ascii=False)
			return render_template('part10.html',part10_active="active",title="Part 10",data = dataJson)
		else:
			return render_template('part10.html',part10_active="active",title="Part 10",information="Your input is wrong!")
	

@app.route('/part11',methods=['GET','POST'])
def part11():
	if request.method=='GET':
		return render_template('part11.html',part11_active = "active",title="Part 11")
	if request.method=='POST':
		low=int(request.form["Low"])
		high=int(request.form["High"])
		if(low>high):
			a=low
			low=high
			high=a
		if low>0 and high>0:
			cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:notminusone.database.windows.net,1433;Database=notminusoneDatabase;Uid=not-1;Pwd={0626Fuyi};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
			cursor = cnxn.cursor()
			cursor.execute("select sum(num),store from f where store>=? and store<=? group by store ",low,high)
			a = cursor.fetchall()
			count=[]
			name=[]
			for item in a:
				count.append(item[0])
				name.append(item[1])
			dic={}
			dic['count']=count
			dic['name']=name
			dataJson=json.dumps(dic,ensure_ascii=False)
			return render_template('part11.html',part11_active = "active",title="Part 11",data = dataJson)
		else:
			return render_template('part11.html',part11_active = "active",title="Part 11",information="Your input is wrong!")


@app.route('/part12',methods=['GET','POST'])
def part12():
	if request.method=='GET':
		return render_template('part12.html',part12_active = "active",title="Part 12")
	if request.method=='POST':
		low=int(request.form["Low"])
		high=int(request.form["High"])
		if(low>high):
			a=low
			low=high
			high=a
		if low>0 and high>0:
			cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:notminusone.database.windows.net,1433;Database=notminusoneDatabase;Uid=not-1;Pwd={0626Fuyi};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
			cursor = cnxn.cursor()
			cursor.execute("select sum(num),store from f where store>=? and store<=? group by store ",low,high)
			a = cursor.fetchall()
			count=[]
			name=[]
			for item in a:
				count.append(item[0])
				name.append(item[1])
			dic={}
			dic['count']=count
			dic['name']=name
			dataJson=json.dumps(dic,ensure_ascii=False)
			return render_template('part12.html',part12_active = "active",title="Part 12",data = dataJson)
		else:
			return render_template('part12.html',part12_active = "active",title="Part 12",information="Your input is wrong!")

@app.route('/part14',methods=['GET','POST'])
def part14():
	if request.method=='GET':
		return render_template('part14.html',part14_active = "active",title="Part 12.5")
	if request.method=='POST':
		latitude1 = float(request.form["latitude1"])
		latitude2 = float(request.form["latitude2"])
		low_latitude = min(latitude1,latitude2)
		high_latitude = max(latitude1,latitude2)
	
		longitude1 = float(request.form["longitude1"])
		longitude2 = float(request.form["longitude2"])
		low_longitude = min(longitude1,longitude2)
		high_longitude = max(longitude1,longitude2)
		low_mag = float(request.form["low"])
		high_mag = float(request.form["high"])
		cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:notminusone.database.windows.net,1433;Database=notminusoneDatabase;Uid=not-1;Pwd={0626Fuyi};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
		cursor = cnxn.cursor()
		cursor.execute("select id,latitude,longitude,net,place from nquakes2 where latitude between "+str(low_latitude)+" and "+str(high_latitude)+
		" and longitude between "+str(low_longitude)+" and "+str(high_longitude)+" and mag between "+str(low_mag)+" and "+str(high_mag))
		row = cursor.fetchall()
		if row is not None:
			return render_template('part14.html',part14_active = "active",data =row)
		else:
			return render_template('part14.html',part14_active = "active",title="Part 12_5")


@app.route('/part13',methods=['GET','POST'])
def part13():
	if request.method=='GET':
		cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:notminusone.database.windows.net,1433;Database=notminusoneDatabase;Uid=not-1;Pwd={0626Fuyi};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
		cursor = cnxn.cursor()
		cursor.execute("select x,y,color from p where color='r'")
		a = cursor.fetchall()
		count=[]
		color=[]
		for item in a:
			count.append(list(item[0:2]))
			color.append(item[2])
		dic={}
		dic['count']=count
		dic['color']=color
		dataJson=json.dumps(dic,ensure_ascii=False)
		cursor.execute("select x,y,color from p where color='g'")
		a1 = cursor.fetchall()
		count1=[]
		color1=[]
		for item in a1:
			count1.append(list(item[0:2]))
			color1.append(item[2])
		dic1={}
		dic1['count']=count1
		dic1['color']=color1
		dataJson1=json.dumps(dic1,ensure_ascii=False)
		return render_template('part13.html',part13_active = "active",title="Part 13",data = dataJson,data1 = dataJson1)		

	
		
		# if id =="":
		# 	cursor.execute("select top(6)* from nquakes2 where net=? order by time desc ",net)
		# 	data = cursor.fetchall()
		# 	if len(data) > 0:
		# 		return render_template('part13.html',part13_active = "active",title="Part 13",data=data)
		# 	else:
		# 		return render_template('part13.html',part13_active = "active",title="Part 13")
		
		# else:
		# 	place = request.form["place"]
		# 	cursor.execute('update nquakes2 set place='+place+" where id="+id)
		# 	return render_template('part13.html',part13_active = "active",title="Part 13")

@app.route('/delete',methods=['POST'])
def delete():
	quakeid = request.form["quakeid"]
	cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:notminusone.database.windows.net,1433;Database=notminusoneDatabase;Uid=not-1;Pwd={0626Fuyi};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
	cursor = cnxn.cursor()
	cursor.execute("delete  from nquakes2 where id=?",quakeid)
	cursor.commit()
	return render_template('part13.html',part13_active = "active",title="Part 13",information="Deletion succeeded!")

@app.route('/edit',methods=['POST'])
def edit():
	quakeid = request.form['quakeid']
	place = request.form["place"]
	cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:notminusone.database.windows.net,1433;Database=notminusoneDatabase;Uid=not-1;Pwd={0626Fuyi};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
	cursor = cnxn.cursor()
	cursor.execute("update nquakes2 set place=? where id=?",place,quakeid)
	cursor.commit()
	cursor.execute("select * from nquakes2 where id=?",quakeid)
	row = cursor.fetchone()
	return render_template('part13.html',part13_active = "active",title="Part 13",information="Modified succeeded!",newdata=row)

@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
	return render_template('404.html',title='404')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
	return render_template('500.html',title='500')


if __name__ == '__main__':
	app.run()