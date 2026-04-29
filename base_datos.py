import sqlite3

conexion = sqlite3.connect("mi_base.db")

cursor = conexion.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            edad INTEGER,
            email TEXT UNIQUE
        )
''')

#en la base de datos se usa el lenguaje SQL para insertar datos, consultar, actualizar o eliminar registros.
cursor.execute("""
    INSERT INTO usuarios (nombre, edad, email) 
    VALUES ('Ratoncito Pérez', 4, 'dientes2@example.com')
               
""")


conexion.commit()

#con este se creo la base de datos 