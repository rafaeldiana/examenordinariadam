import sqlite3 as lite
import sys

conexion = lite.connect("agenda.sqlite")

cursor = conexion.cursor()
cursor.execute("SELECT SQLITE_VERSION()")
datos = cursor.fetchone()
print("La versión de SQLite es:",datos)

