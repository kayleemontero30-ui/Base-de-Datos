import sqlite3

conexion = sqlite3.connect("mi_base.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM usuarios") #QUERY MAS SIMPLE, devuelve todos los usuarios de la base de datos

resultados = cursor.fetchall() #fetchall() devuelve todos los resultados de la consulta en forma de lista de tuplas

for fila in resultados:
    print(fila)#como se esta imprimiendo cada fila, se muestra cada usuario como una tupla con sus datos (id, nombre, edad, email)