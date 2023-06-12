import sqlite3 as lite
import sys

conexion = lite.connect("agenda.sqlite")

cursor = conexion.cursor()
cursor.execute("UPDATE contactos SET telefono = '12345678';")

conexion.commit()
