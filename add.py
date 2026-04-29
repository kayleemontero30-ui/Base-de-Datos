import sqlite3

conexion = sqlite3.connect("mi_base.db")

cursor = conexion.cursor()

#se pueden insertar datos en la base de datos a traves de cualquier archivo 

while True:
    nombre = input("Dime el nombre del usuario: ")
    edad = int(input("Dime la edad del usuario: ")) #la edad tiene que tener int ya que sera un numero entero 
    email = input("Dime el email del usuario: ")
    cursor.execute(f"""
    INSERT INTO usuarios (nombre, edad, email) 
    VALUES ('{nombre}', {edad}, '{email}')
               
""")
    #las comillas simples se usan dentro de la consulta SQL para delimitar los valores de texto, como el nombre y el email.
    #las comillas dobles se usan para delimitar la cadena de texto en Python que contiene la consulta SQL. Esto permite que las comillas simples dentro de la consulta SQL no interfieran


    conexion.commit()

    print(f"{nombre} ha sido agregado a la base de datos.")
    continuar = input("¿Quieres agregar otro usuario? (si/no): ")
    if continuar.lower() != 'si':
        break