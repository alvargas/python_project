# String (Datatypes). 

mySTR = "Hello World"

# Métodos o funciones (variable.método())
print(mySTR.upper())
print(mySTR.lower())
print(mySTR.swapcase()) # Invierte MY a mn y viceversa
print(mySTR.capitalize()) # La primera letra de la frase en MY.
print(mySTR.replace('Hello', 'Bye').upper()) # Métodos encadenados
print(mySTR.count(' '))

print(mySTR.startswith('hel')) # False. El texto inicia con 'Hel'
print(mySTR.endswith('rld')) # True

print(mySTR.split()) # Separa a partir de un space. Y crea una lista
print(mySTR.split('o')) # Separa a partir de un caractér.

print(mySTR.find('l')) # Devuelve la posición de la primera 'l'. (2)

print(len(mySTR)) # 11
print(mySTR.index('W')) # 6

print(mySTR.isnumeric())
print(mySTR.isalpha())

print(mySTR[6]) # W
print(mySTR[-1]) # d (conteo a la inversa)

print("El saludo es: " + mySTR)
print(f"El saludo es: {mySTR}") # f interpreta la variable (Vers 6.3+)
print("El saludo es: {0}".format(mySTR)) # Igual resultado.
print ("")
print ("Métodos y sus propiedades de strings: ", (dir(mySTR)))

