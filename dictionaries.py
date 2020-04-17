# Dictionaries (Datatypes) {}
# Permite definir un dato a partir de claves y valores.
# Dicionario de datos. Un conjunto de datos, conformados por claves y valores
# Una clave puede ser una tupla y un valor puede ser un nombre
# Definen objetos de la vida real: una persona, un producto
# Los diccionarios se pueden agrupar dentro de una lista.
# las claves siempre van entre "".

# ejemplo para carrito de compras
product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

person = {
    "first_name": "Jhon",
    "last_name": "Queen"
}

print(type(person)) # <class dict>

#print(dir(product))

print(product.keys()) # sólo las claves del diccionario "product"
print(product.values()) # sólo los valores del diccionario "product"
print(product.items()) # todos los ítems del diccionario "product"

#del person

print(person.clear()) # muestra None porque modifica datos
person.clear() # modifica
print(person) # lee

# Diccionarios en una lista
products = [
    {"name": "book", "price": 25.40},
    {"name": "laptop", "price": 375.25}
]
print(products) # genera un arreglo con 2 diccionarios
