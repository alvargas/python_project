# Las funciones son código ya escrito internamente en el lenguaje
# Le damos valores a la f, se ejecuta y nos devuelve un elemento o un resultado 
# Poseer funciones es una de las partes más fuertes de un lenguaje.
# Nos permiten reutilizar código 

# Definir nuestras propias funciones

def hola():
    print("hellO woRLD") # el código no se ejecuta hasta llamar la función
hola() # llamado a la función. Ejecuta el código

# Saludando a alguien
def hola(name): # name es un parámetro definido para la f
    print("HellO", name)
    #print("HellO " + name) # concatenado
hola("John") # "John" es el valor

# No sólo sirve para encapsular código sino también para reutilizarlo
hola("Myke")
hola("Katy")

# Parámetros o argumentos ( ("Carol") ) por defecto
def hola(name="Carol"):
    print("Hola", name)
hola()

# Retornar un valor
def add(number_one, number_two):
    return number_one + number_two
print(add(20, 10)) # se está reutlizando código ya escrito (lineas anteriores)

# Algunas funciones preconstruidas: print()  dir()  type()  len()
print(len("hello"))

# Funciones Lambda. Son funciones anónimas que toman un número de argumentos pero que tan sólo pueden ser 
# escritas utilizando una sola expresión (una línea de código) 
suma = lambda number_one, number_two: number_one + number_two # función suma con 2 parámetros, los suma.
print(suma(35, 25))




# video en 2:54