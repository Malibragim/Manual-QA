# -*- coding: utf-8 -*-
"""Создание базы данных и простые запросы.ipynb"


Original file is located at
    https://colab.research.google.com/drive/1oJ3CTr63yXlsJkAj-xsmt1BcCQwvmpLX

## Импортируем библиотеку sqlite3
"""

import sqlite3

my_database = sqlite3.connect('database.db')
cur = my_database.cursor()
my_database.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
        userid INT PRIMARY KEY,
        fname TEXT,
        lname TEXT,
        gender TEXT,
        age INT);
      """)
my_database.commit()

cur.execute("""INSERT INTO users(userid, fname, lname, gender)
VALUES
       ('5', 'Luke', 'Rockhold', 'male');""")
my_database.commit()

cur.execute("SELECT * FROM users;")
one_result = cur.fetchall()
print(one_result)

cur.execute("""DELETE FROM users WHERE fname='Luke';""")
my_database.commit()

cur.execute("SELECT * FROM users;")
one_result = cur.fetchall()
print(one_result)
