# Loops, bucles o iteradores. For & While

foods = ["aples", "bread", "cheese", "milk"] 
for food in foods: # recorre cada elemento de foods
    if (food=="bread"):
        print("Tienes que comprar pan") 
        continue # ignora la condición del if y continúa
        #break # se ejecuta la instrucción anterior (print) y termina el bucle
    print(food)

# Recorrer un rango
for number in range(1, 8): # number es como una variable recien creada
    print(number) # llega hasta un número antes del rango.

for letter in "hello":
    print(letter) # muestra todos los caracteres
print('') # Verificar (espacio?)

# While
count = 4
while count <=10:
    print(count)
    count = count + 1
#Pruebas con commit. diff  refleja sólo lo que se agrega, no muestra nada de lo que se quita?
#Nueva linea en fin de archivo.