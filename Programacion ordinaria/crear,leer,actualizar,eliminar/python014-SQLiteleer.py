import sqlite3 as lite
import sys

conexion = lite.connect("agenda.sqlite")

cursor = conexion.cursor()
cursor.execute("SELECT * FROM contactos;")

datos = cursor.fetchall()

for i in datos:
    print("ID:",i[0],"nombre:",i[1],"\t telefono: ",i[2],"\t email:",i[3])

