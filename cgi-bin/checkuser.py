#!/usr/bin/env python3
from form import *
from index import *
import sqlite3
import hashlib

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

def auth(login,passw):
	con = sqlite3.connect('./storage/database.db')
	cursor = con.cursor()
	cursor.execute('SELECT * FROM users WHERE loging = "{}"'.format(login))
	rows = cursor.fetchall()
	if len(rows) == 0:
		signup()
		nouser()		
	else:
		if check_password(rows[0][2], passw):
			cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
			name = cookie.get("name")
			print("Set-cookie: name={}; max-age=1200".format(rows[0][1]))
			tabs(login)
		else:
			signup()
			incorrectpass()

form = cgi.FieldStorage()
login = html.escape(form['login'].value)
passw = html.escape(form['password'].value)
auth(login, passw)