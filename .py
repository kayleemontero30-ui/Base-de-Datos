import sqlite3

conexion = sqlite3.connect("mi_base.db")

cursor = conexion.cursor()

cursor.execute("""
    UPDATE usuarios
    SET edad = 3
    WHERE nombre = 'Juan Pérez'

""")

conexion.commit()