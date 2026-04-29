import sqlite3

conexion = sqlite3.connect("mi_base.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM usuarios WHERE email LIKE '%@uax.es' OR email LIKE '%@uax.com'") #se seleccionan los usuarios cuyo email termina con @uax.es o @uax.com
#QUERY MAS SIMPLE, devuelve todos los usuarios de la base de datos (SELECT)

#WHERE se usa para filtrar los resultados de la consulta, en este caso, solo se seleccionan los usuarios cuya edad es mayor a 3 años.

resultados = cursor.fetchall() #fetchall() devuelve todos los resultados de la consulta en forma de lista de tuplas
for fila in resultados:
    print(fila)#como se esta imprimiendo cada fila, se muestra cada usuario como una tupla con sus datos (id, nombre, edad, email)