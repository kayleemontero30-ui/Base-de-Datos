import sqlite3

conexion = sqlite3.connect("mi_base.db")
cursor = conexion.cursor()

cursor.execute("SELECT count (*) FROM usuarios WHERE email NOT LIKE '%@uax.com'") #se seleccionan los usuarios cuyo email termina con @uax.es o @uax.com
#QUERY MAS SIMPLE, devuelve todos los usuarios de la base de datos (SELECT)

#WHERE se usa para filtrar los resultados de la consulta, en este caso, solo se seleccionan los usuarios cuya edacd es mayor a 3 años.
#% es un comodín que representa cualquier secuencia de caracteres, por lo que '%@uax.es' coincide con cualquier email que termine con '@uax.es'.
#OR se usa para combinar dos condiciones, en este caso, se seleccionan los usuarios cuyo email termina con '@uax.es' o '@uax.com'.
# LIKE se usa para buscar un patrón específico en una columna, en este caso, se busca cualquier email que termine con '@uax.es' o '@uax.com'.
#count (*) se usa para contar el número de filas que cumplen con la condición especificada en la cláusula WHERE. En este caso, se cuenta el número de usuarios cuyo email termina con '@uax.es' o '@uax.com'.
# NOT se usa para negar una condición, en este caso, se seleccionan los usuarios cuyo email NO termina con '@uax.es' o '@uax.com'.
resultados = cursor.fetchall() #fetchall() devuelve todos los resultados de la consulta en forma de lista de tuplas

for fila in resultados:
    print(fila)#como se esta imprimiendo cada fila, se muestra cada usuario como una tupla con sus datos (id, nombre, edad, email)