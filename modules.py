# 1. Modulos propios. Los que creamos
# 2. Modulos descargados (Third party modules)
# 3. Modulos o bibliotecas de Python
# Los módulos serían la parte principal de la aplicación. Luego están las funciones
# Hay que buscar los módulos en internet los módulos precontruidos de Python.
# Ej. Python modules. pip modules. pypi,org: modulos creados por la comunidad.

# Modulos preconstruidos de Python
import datetime
print(datetime.date.today()) # datetime, el módulo; date, el parámetro; today, el método.
print(datetime.timedelta(minutes=75)) # método timedelta()

from datetime import timedelta, date
print(timedelta(minutes=80)) # método timedelta() importado directamente
print(date.today()) # método date() importado directamente

# Modulos propios
import fmath # importa todo el código de fmath.py

# Utilizando el modulo propio importado fmath:
fmath.add(1,2) # método add(); parámetros 1 y 2.
fmath.substract(1,2)

# Importando directamente las 2 funciones: add y substract.
from fmath import add, substract
add(1,2)
substract(1,2)

# Importando otros módulos de terceros: colorama
# En pypi.org buscamos colorama (ver su documentación)
# pip install colorama # lo instalamos

from colorama import Fore, Style, init
print(Fore.RED, "Hello World") # En la consola de Windows se genera de color blanco

init(convert=True) # permite dar salida al color deseado en la consola de Windows
print(Fore.RED, "Hello World") 

# pip install Flask o django (Frameworks para crear aplicaciones web)
# Biblioteca tkinter, que permite diseñar GUIs, de escritorio. 

# Temas pendientes:
    #POO, Clases, programación funcional, 