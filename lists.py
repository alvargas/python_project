# List (Datatypes) []

my_list = [1, "hello", 1.34, True, [1, 2, 3]]
print(len(my_list)) # 5
colors = ["red", "green", "blue"]
print(colors[-1])
print ("La lista 'colors' es de tipo: ", (type(colors)))
print('green' in colors) # True
print(colors)
colors[1] = "yellow"
print(colors)
colors.append("pink") # Agregar un elemento al final
print(colors)
colors.extend(["orange",'cyan','with']) # Agregar varios elementos (como lista)
print(colors) # Igual desde tupla o lista, agrega al final
#colors.extend(("cyan", "with")) # Agregar varios elementos (como tupla)
#print(colors) # Igual desde tupla o lista, agrega al final

colors.insert(1, "black")
print(colors)
colors.insert(-1, "orange")
print(colors)
colors.insert(len(colors), "gray")
print(colors)

colors.pop() # Elimina el último elemento de la lista
colors.pop() # Elimina el último elemento de la lista (como el anterior)
colors.pop(2) # Elimina el tercer elemento de la lista
print(colors)

colors.remove('cyan')
print(colors)

colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)

print("Índice de color pink:", colors.index('orange'))

print(colors.count('orange'))

colors.clear()  # Quita todos los elementos de la lista y la deja vacía.
print(colors)

# Constructor. A partir de la función list()
print ("")
number_list = list((1, 2, 3, 4)) # No se pasa como lista. (1,2,3,4) es Tupla. 
print(number_list)

r = list(range(1, 21))
print(r)

print ("")
print ("Métodos y sus propiedades de una lista: ", (dir(colors)))

#colors.pop()
