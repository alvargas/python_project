# Tuples (Datatypes) ()
# Conjunto de datos como las listas, pero que no podemos cambiar.
# La tupla es un valor inmutable. El código se ejecuta más rápido.
# Uso real de la tupla: diccionarios  o listas (ver al final) 

x = (5, 10, 15, 20) # Método más usado
print(x, type(x))
month = ('Enero', "Febrero", 'Marzo', 'Abril')
print(month)
print(month[2])
print(month.index('Abril'))

#x[2] = 30 # Las tuplas no soportan reasignación.

# Constructor. A partir de la función tuple()
y = tuple((5, 10, 15))
print(y)

z = (3)
print("tupla de un elemento:", z, type(z)) # No es considerado tupla sino lista. 

z = (3,)
print("tupla de un elemento:", z, type(z)) # Considerado tupla. 

del x 
#print(x)

print ("")
print ("Métodos y sus propiedades de una tupla: ", (dir(y)))

""" locations{
    (36.24343434, 75.23222): "Tokio",
    (24.43333334, 91.03232): "New York"
}
 """
