# This will set up a local database using mysql. It will later be used by the python project.

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="",
  password=""
)

print(mydb)