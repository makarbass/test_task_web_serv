#!/usr/bin/env python3
import sqlite3
from index import *
from form import *

if cookietest() == True:
	cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
	name = cookie.get("name")
	tabs(name.value)
	form = cgi.FieldStorage()
	value = form['btn'].value
	con = sqlite3.connect('./storage/database.db')
	cursor = con.cursor()
	cursor.execute('SELECT * FROM places WHERE name="{}"'.format(value))
	place = cursor.fetchall()
	if place[0][2] == 1:
		cursor.execute('SELECT * FROM places WHERE userlogin = ?', (name.value,))
		records = cursor.fetchall()
		if len(records) != 0:
			print("""
				<div class="alert">
		 Вы уже сидите на другом месте!
		</div>
				""")
		else:	
			print("<div> Занять место {}.</div>".format(place[0][1]))
			print("""
			<form action="/cgi-bin/changeplace.py">
				<div class="col">
		        <input type="text" name="name" placeholder="Фамилия Имя Отчество" required>
		        <input type="hidden" name="place" value="{}">
		        <input type="hidden" name="user" value="{}">
		        <input type="submit" value="Занять">
		      </div>
		    </form>
			""".format(place[0][1], name.value))
	else:
		print("<div> Место {} занято {}".format(place[0][1],place[0][4]))
		if place[0][3] == name.value:
			print("<strong>(Вы)</strong>. </div>")
			print("""
		<form action="/cgi-bin/changeplace.py">
		<div class="col">
			<input type="hidden" name="name" value="{}">
			<input type="hidden" name="place" value="{}">
	        <input type="submit" value="Освободить место">
	      </div>
	    </form>
			""".format(place[0][4],place[0][1]))
	footer()
else:
	signup()