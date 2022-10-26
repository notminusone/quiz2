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


@app.route('/')
def part10():
	data = []
	frults = ['apple','pear','berry','grape','kiwi','banana']
	cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:notminusone.database.windows.net,1433;Database=notminusoneDatabase;Uid=not-1;Pwd={0626Fuyi};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
	cursor = cnxn.cursor()
	for frult in frults:
		cursor.execute("select sum(num) from f where food=?",frult)
		row = cursor.fetchone()
		data.append(int(row))
	
	return render_template('part10.html',part10_active="active",title="Part 10",data=data)
	

@app.route('/part11',methods=['GET','POST'])
def part11():
	data = []
	frults = ['apple','pear','berry','grape','kiwi','banana']
	cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:notminusone.database.windows.net,1433;Database=notminusoneDatabase;Uid=not-1;Pwd={0626Fuyi};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
	cursor = cnxn.cursor()
	for frult in frults:
		cursor.execute("select sum(num) from f where food=?",frult)
		row = cursor.fetchone()
		data.append(int(row))
	
	return render_template('part11.html',part11_active="active",title="Part 11",data=data,frults=frults)
	# if request.method=='GET':
	# 	return render_template('part11.html',part11_active = "active",title="Part 11")
	# if request.method=='POST':
	# 	low = float(request.form["low"])
	# 	high = float(request.form["high"])
	# 	N = int(request.form["N"])
	# 	cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:notminusone.database.windows.net,1433;Database=notminusoneDatabase;Uid=not-1;Pwd={0626Fuyi};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
	# 	cursor = cnxn.cursor()
	# 	data = []
	# 	step = (high-low)/N
	# 	for i in range(N):
	# 		cursor.execute("select count(*) from nquakes2 where mag>"+str(low + step * i)+ "and mag<"+ str(low + step * (i + 1)))
	# 		num = cursor.fetchval()
	# 		cursor.execute("select max(mag) from nquakes2 where mag>"+str(low + step * i)+ "and mag<"+ str(low + step * (i + 1)))
	# 		max = cursor.fetchval()
	# 		cursor.execute("select time,place from nquakes2 where mag=?",max)
	# 		row = cursor.fetchone()
	# 		data.append({
	# 			"num":num,
	# 			"time":row[0],
	# 			"place":row[1]
	# 		})
	# 	if len(data) > 0:
	# 		return render_template('part11.html',part11_active = "active",title="Part 11",data=data)
	# 	else:
	# 		return render_template('part11.html',part11_active = "active",title="Part 11")

@app.route('/part12',methods=['GET','POST'])
def part12():
	if request.method=='GET':
		return render_template('part12.html',part12_active = "active",title="Part 12")
	if request.method=='POST':
		latitude1 = float(request.form["latitude1"])
		latitude2 = float(request.form["latitude2"])
		low_latitude = min(latitude1,latitude2)
		high_latitude = max(latitude1,latitude2)
	
		longitude1 = float(request.form["longitude1"])
		longitude2 = float(request.form["longitude2"])
		low_longitude = min(longitude1,longitude2)
		high_longitude = max(longitude1,longitude2)
		cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:notminusone.database.windows.net,1433;Database=notminusoneDatabase;Uid=not-1;Pwd={0626Fuyi};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
		cursor = cnxn.cursor()
		# cursor.execute("select id,latitude,longitude,net,place from nquakes2 where latitude=?",latitude," and longitude=?",longitude)
		cursor.execute("select id,latitude,longitude,net,place from nquakes2 where latitude between "+str(low_latitude)+" and "+str(high_latitude)+
		" and longitude between "+str(low_longitude)+" and "+str(high_longitude))
		row = cursor.fetchall()
		if row is not None:
			return render_template('part12.html',part12_active = "active",data =row)
		else:
			return render_template('part12.html',part12_active = "active",title="Part 12",information="no data be searched")

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
		return render_template('part13.html',part13_active = "active",title="Part 13")
	if request.method=='POST':
		net = request.form["net"]
		cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:notminusone.database.windows.net,1433;Database=notminusoneDatabase;Uid=not-1;Pwd={0626Fuyi};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
		cursor = cnxn.cursor()
		cursor.execute("select top(6)* from nquakes2 where net=? order by time desc ",net)
		data = cursor.fetchall()
		if len(data) > 0:
			return render_template('part13.html',part13_active = "active",title="Part 13",data=data)
		else:
			return render_template('part13.html',part13_active = "active",title="Part 13")
		
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