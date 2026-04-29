import sqlite3

conexion = sqlite3.connect("mi_base.db")

cursor = conexion.cursor()

#en la base de datos se usa el lenguaje SQL para insertar datos, consultar, actualizar o eliminar registros.
cursor.execute("""
    UPDATE usuarios 
    SET edad = 40
    WHERE id = 4      
""")


conexion.commit()
