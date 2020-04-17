# Condicionales. Control de flujo de programas 
# True o False

x = 40
if x < 30:
    print("x es menor que 30") # el valor no se muestra porque es falso

x = 10
if x < 30:
    print("x es menor que 30") # imprime el mensaje

x = 20 # un = es asignación de valor
if x == 20: # == es comparación, equivalencia. 
    print("x equivale a 20")    

x = 20
if x < 15:
    print("x es menor que 15")
else:
    print("x es mayor que 15")

x = "blue"
if x == "red":
    print("x es red")
elif x == "blue":
    print("x es blue")
else:
    print("x no es red")

print('')
name = "John"
last_name = "Carter"

if name == "John":
    if last_name == "Cartier":
        print("Tú eres John Carter")
    else:
        print("Tú no eres John Carter")
else:
    print("Tú no eres John") # si esto se cumple, no recorre el if anidado

# Comprobar si un número está entre 2 y 10
x=0
if x > 2 and x <= 10:
        print("x es mayor que 2 y menor o igual a 10")

if x > 2 or x <= 20:
        print("x es mayor que 2 o menor o igual a 20")

y=1
if (not(x==y)):
    print("x no es igual a y")
else:
    print("x es igual a y")
       







