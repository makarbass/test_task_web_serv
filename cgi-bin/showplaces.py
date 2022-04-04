#!/usr/bin/env python3
from form import *
from index import *
import sqlite3

def showlog(rows):
	print(""" 
	<table>
	  <tr>
	  	<th>№</th>
	    <th>Логин</th>
	    <th>Место</th>
	    <th>Начало</th>
	    <th>Конец</th>
	  </tr>
		""")
	for i in range(len(rows)):
		print("<tr>")
		for j in range(len(rows[i])):
			if (rows[i][j] == '' or rows[i][j] is None):
				print("""
		    	<td>{}</td>
					""".format("🖥 На месте "))
			else:
				print("""
		    	<td>{}</td>
					""".format(rows[i][j]))
		print("</tr>")
	print("</table>")

def history(cursor,name):
	if cookietest() == True:
		tabs(name)
		cursor.execute('SELECT * FROM logtime ORDER BY id DESC')
		rows = cursor.fetchall()
		showlog(rows)
	else:
		signup()

def places(cursor,name):
	if cookietest() == True:
		tabs(name)
		a = ""
		cursor.execute('SELECT * FROM places')
		places = cursor.fetchall()
		print("""
			<div>
			<form action="/cgi-bin/logs.py">""")
		for i in range(len(places)):
			if places[i][2] == 1:
				print('<button value="{}" name="btn" type="submit" class="btn-group-green">{}</button>'.format(places[i][1],places[i][1]))
			else:			
				print('<button value="{}" name="btn" type="submit" class="btn-group-red">{}</button>'.format(places[i][1],places[i][1]))
		print("""</form>
			</div>""")
	else:
		signup()

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")
form = cgi.FieldStorage()
con = sqlite3.connect('./storage/database.db')
cursor = con.cursor()
if form['tab'].value == 'place':
	places(cursor,name.value)
if form['tab'].value == 'history':
	history(cursor,name.value)
if form['tab'].value == 'exit':
	cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
	name = cookie.get("name")
	print("Set-cookie: name={}; max-age=0".format(name))
	signup()

