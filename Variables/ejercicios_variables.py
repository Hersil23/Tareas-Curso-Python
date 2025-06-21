# creacion de una variable escrita en el idioma ingles, que representa el apellido de una persona   

lastName = "Silva"  

"""
Me gustaria crear un bot para responder mensajes de whatapp, 
instagran, telegram y correos electronicos.
"""

#Ejecicios de variables y tipos de datos
# 1. Declaracion de variables
#  Declara una variable city y asígnale el nombre de tu ciudad.

city = "Madrid"

# - Declara una variable actual_Temp y asígnale un valor flotante que represente la temperatura.

actual_Temp = 22.5

#  - Declara una variable have_pets y asígnale un valor booleano.

have_pets = True

# - Declara una variable birthdate y asígnale tu año de nacimiento como un entero.

birthdate = 1978

""" 
2. Impresión de variables: Imprime en la consola cada una de las variables que declaraste
		en el ejercicio anterior, junto con un mensaje descriptivo para cada una 
		(por ejemplo: "Mi ciudad es:", "La temperatura actual es:").
"""
print("Mi ciudad es:", city)
print("La temperatura actual es:", actual_Temp)
print("¿Tengo mascotas?", have_pets)
print("Mi año de nacimiento es:", birthdate)

"""
3. Asignación múltiple* Asigna en una sola línea los valores "Perro", 5 y True a las variables 
		animal, animal_age  y is_a_mammal respectivamente. Luego, imprime los valores de cada variable.
"""

animal, animal_age, is_a_mammal = "Perro", 5, True
print("Animal:", animal)
print("Edad del animal:", animal_age)
print("¿Es un mamífero?", is_a_mammal)

"""
Ejercicios de Listas
1. Creación de listas:
    - Crea una lista llamada colors con al menos cinco colores diferentes.
    - Crea una lista llamada prices con al menos cinco números decimales.
    - Crea una lista mix que contenga una cadena de texto, un número entero, 
    un booleano y otra lista anidada.
"""

colors = ["Rojo", "Azul", "Verde", "Amarillo", "Naranja"]
prices = [10.99, 5.49, 3.75, 8.20, 12.00]
mix = ["Hola, Python", 42, True, ["Tarea1", "Tarea2", "Tarea3"]]

"""
2. Acceso a elementos (Deben investigar):
    - Imprime el tercer elemento de la lista colors.
    - Imprime el último elemento de la lista prices.
    - Accede e imprime el segundo elemento de la lista anidada dentro de tu lista mix.

"""
print("Tercer color:", colors[2])
print("Último precio:", prices[-1])	
print("Segundo elemento de la lista anidada:", mix[3][1])

"""
Ejercicios de Tuplas

1. Creación de tuplas:
    - Crea una tupla llamada week_Days con los siete días de la semana.
    - Crea una tupla coordinates con dos números flotantes que representen una latitud y una
		longitud.
2. Acceso a elementos (Deben investigar):
    - Imprime el segundo elemento de la tupla coordinates.

"""

week_Days = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

coordinates = (40.4168, -3.7038)  # Latitud y longitud de Madrid

print("La longitud de Madrid es:", coordinates[1])

"""
Ejercicios de Diccionarios

1. Creación de diccionarios:
    - Crea un diccionario llamado book con las siguientes claves y valores: "titulo" (string), 
      "autor" (string), "año_publicacion" (entero), "disponible" (booleano).
    - Crea un diccionario students que contenga su nombre, edad, carrera y una lista de sus 
      materias favoritas.
2. Acceso de diccionarios (Deben investigar):
    - Imprime el autor del book.
3. Combinación de conceptos (Opcional para investigar y realizar):
    - Crea una lista de diccionarios donde cada diccionario represente un producto con claves 
      como "nombre", "precio" y "cantidad".
    - Accede al nombre del segundo producto en tu lista de diccionarios.
"""

book = {
		"titulo": "Juan Salvador Gaviota",
		"autor": "Richard Bach",
		"año_publicacion": 1970,
		"disponible": True
}

students = {
		"nombre": "Herasi",
		"edad": 47,
		"carrera": "Desarrollo Web",
		"materias_favoritas": ["Tailwind", "Programacion en Python", "CSS"]
}

print("Autor del libro:", book["autor"])

products = [
		{"nombre": "Audifonos inalambricos F9-5", "precio": 8, "cantidad": 12},
		{"nombre": "Audifonos inalambricos Earphone 2nd Generation.", "precio": 8, "cantidad": 10},
		{"nombre": "Audifonos inalambricos M19", "precio": 9, "cantidad": 14}
]

print("Nombre del segundo producto:", products[1]["nombre"])


