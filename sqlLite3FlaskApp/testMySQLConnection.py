import random
from datetime import datetime, timedelta

import requests

import mysql.connector

localHost = "http://localhost"
port = "5050"

r = requests.get(f"{localHost}:{port}/usersArchive", params={"where":"frequency < 2450"})
print(r)


import pymysql
conn = pymysql.connect(
    host="127.0.0.1",
    user="user",
    password="userpass",
    database="mydb"
)
cursor = conn.cursor()
cursor.execute("SELECT * from users")
print(cursor.fetchone())

# Close the connection
cursor.close()
conn.close()

print("Completed")





