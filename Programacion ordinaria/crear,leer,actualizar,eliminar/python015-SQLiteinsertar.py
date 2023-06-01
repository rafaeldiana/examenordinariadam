import sqlite3 as lite
import sys

conexion = lite.connect("agenda.sqlite")

cursor = conexion.cursor()
cursor.execute("INSERT INTO contactos VALUES(NULL,'Jorge','222222','jorgecorreo');")

conexion.commit()
