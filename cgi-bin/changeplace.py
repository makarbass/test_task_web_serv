#!/usr/bin/env python3
from index import *
from datetime import datetime
from form import *
import sqlite3

if cookietest() == True:
	cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
	name = cookie.get("name")
	form = cgi.FieldStorage()
	now = datetime.now()
	d1 = now.strftime("%d/%m/%Y %H:%M:%S")
	con = sqlite3.connect('./storage/database.db')
	cursor = con.cursor()

	if len(form) == 3:
		entities = (form['name'].value,form['place'].value,d1)
		cursor.execute('INSERT INTO logtime(user_login, place, start) VALUES(?, ?, ?);', entities)
		column_values = (0, form['user'].value, form['name'].value, form['place'].value)
		cursor.execute('UPDATE places SET isfree = ?, userlogin = ?, fio = ? WHERE name = ?', column_values)
		con.commit()
		tabs(name.value)
	else:
		entities = (d1, form['place'].value, form['name'].value)
		cursor.execute('UPDATE logtime SET finish = ? WHERE place = ? AND user_login = ?;', entities)
		column_values = (1, ' ',' ', form['place'].value)
		cursor.execute('UPDATE places SET isfree = ?, userlogin=?, fio =?  WHERE name = ?', column_values)
		con.commit()
		tabs(name.value)
else:
	signup()