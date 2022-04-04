#!/usr/bin/env python3
from datetime import datetime
from index import *
import os
import http.cookies

def tabs(name):
	header()
	print("""
	<p>Привет, {}.</p>
	<div class="tab">
			<form action="/cgi-bin/showplaces.py">
  		<button type="submit" name="tab" value="place" class="tablinks">Выбрать место</button>
  		<button type="submit" name="tab" value="history" class="tablinks">История авторизации</button>
  		<button type="submit" name="tab" value="exit" class="tablinks">Выйти</button>
  		</form>
	</div>
		""".format(name))

def nouser():
	print("""
		<div class="alert">
 Пользователь не найден!
</div>
		""")

def incorrectpass():
		print("""
		<div class="alert">
 Неверный пароль!
</div>
		""")

def cookietest():
	cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
	name = cookie.get("name")
	if name.value != 'value':
	 	return True
	else:
	 	return False