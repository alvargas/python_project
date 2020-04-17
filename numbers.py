# Numbers (Datatypes). 

# print(type(9))
# print(type(9.4))
# print(2**4)
# print(3/2) # 1.5 (float)
# print(3//2) # 1 (Valor o parte entero)
# print(3%2) # 1 (Residuo). Operador de Módulo
# print((20 - 10) / 5 * 3**2) # 1.5 Tabla de precedencia. (),/,*,**

edad = input("Inserta tu edad: ") # Todo lo digitado es string
print(type(edad))
#new_edad = edad + 5 # Error. string (valor digitado) + entero (5)
new_edad = int(edad) + 5
print(new_edad) 
print(type(new_edad))

