#!/usr/bin/env python3
import cgi
import html

def header():
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href="../styles/style.css">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

def footer():
    print("""</body>
        </html>""")

def signup():
    header()
    print("""
<div class="container">
  <form action="/cgi-bin/checkuser.py" method="post">
    <div class="row">
      <h2 style="text-align:center">Войти в личный кабинет</h2>
      <div class="col">
        <input type="text" name="login" placeholder="Имя пользователя" required>
        <input type="password" name="password" placeholder="Пароль" required>
        <input type="submit" value="Войти">
      </div>
    </div>
  </form>
</div>""")
    footer()