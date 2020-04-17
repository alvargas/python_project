# Sets (Datatypes) {}
# Set es una colección desordenada sin un índice.
# Para acceder a su valores, se debe hacer de otra forma, no a partir de un índice.
# es como lista, pero sin índice. 
x = {'red', 'green', 'blue'}
print(x)
print(type(x)) # type set
print('blue' in x)

x.add('yellow') # No lo agrega al final ni al inicio. No tiene índice
print(x)

x.remove('green')
print(x)

x.clear()
print(x)

#del x # se elimina igual que en una tupla.
#print(x)

