import sys
import tty
import termios
"""1 - Crea un comentario en el código y coloca la URL del sitio web oficial del
       lenguaje de programación que has seleccionado."""

#https://python.org

"""2 - Representa las diferentes sintaxis que existen de crear comentarios
       en el lenguaje (en una línea, varias...)."""

#Comentario de una linea
"""Comentario de un bloque Linea 1
   Comentario de un bloque Linea 2"""

"""3 - Crea una variable (y una constante si el lenguaje lo soporta)."""
mi_variable = 10
MI_CONSTANTE = 3.14
"""4 - Crea variables representando todos los tipos de datos primitivos
       del lenguaje (cadenas de texto, enteros, booleanos...)."""
cadena_texto = "Hola, Python"
entero = 42
punto_flotante = 3.14159
booleano_verdadero = True
booleano_falso = False
numero_complejo = 1 + 2j

"""5 - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"""""
nombre_lenguaje = input("Ingresar el nombre de tu lenguaje a lección: ")
print('     ¡Hola,',nombre_lenguaje,'!')