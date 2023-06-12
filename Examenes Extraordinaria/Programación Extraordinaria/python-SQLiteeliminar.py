import sqlite3 as lite
import sys

conexion = lite.connect("agenda.sqlite")

cursor = conexion.cursor()
cursor.execute("DELETE FROM contactos WHERE Identificador = 2;")

conexion.commit()
