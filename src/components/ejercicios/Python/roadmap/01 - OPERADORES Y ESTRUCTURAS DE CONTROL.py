import sys
import tty
import termios
"""- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
     Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
     (Ten en cuenta que cada lenguaje puede poseer unos diferentes)"""

print("Operadores Aritméticos")
print("----------------------")
a = 10
b = 3
print("Suma a + b =", a + b)              # 13
print("Resta a - b = ", a - b)             # 7
print("Multiplicación a * b = ", a * b)    # 30
print("División a / b = ", a / b)          # 3.333...
print("Módulo a % b = ", a % b)            # 1
print("Exponenciación a ** b = ", a ** b)   # 1000
print("División Entera a // b = ", a // b)  # 3
print(" ")

print("Operadores de Comparación")
print("-------------------------")
print("Igual a == b = ", a == b)            # False
print("Distinto a != b = ", a != b)         # True
print("Mayor que a > b = ", a > b)         # True
print("Menor que a < b = ", a < b)         # False
print("Mayor o igual que a >= b = ", a >= b) # True
print("Menor o igual que a <= b = ", a <= b) # False
print(" ")

print("Operadores Lógicos")
print("------------------")
x = True
y = False
print("Lógico AND: x and y = ", x and y)      # False
print("Lógico OR: x or y = ", x or y)        # True
print("Lógico NOT: not x = ", not x)        # False
print(" ")

print("Operadores a Nivel de Bits")
print("--------------------------")
print("AND a nivel de bits: a & b =", a & b) # 2
print("OR a nivel de bits: a | b = ", a | b)  # 11
print("XOR a nivel de bits: a ^ b = ", a ^ b) # 9
print("NOT a nivel de bits: ~a = ", ~a)    # -11
print(" ")

print("Operadores de Asignación")
print("------------------------")
c = 5
c += 2
print("c = 5")
print("Asignación de suma: c += 2 = ", c)    # 7
c -= 2
print("Asignación de resta: c -= 2 = ", c)   # 5
c *= 2
print("Asignación de multiplicación: c *= 2 = ", c) # 10
c /= 2
print("Asignación de división: c /= 2 = ", c) # 5.0
c %= 3
print("Asignación de módulo: c %= 3 = ", c)   # 2.0
c **= 2
print("Asignación de exponenciación: c **= 2 = ", c) # 4.0
c //= 3
print("Asignación de división entera: c //= 3 = ", c) # 1.0
c = int(c)
c &= 1
print("Asignación AND a nivel de bits: c &= 1 = ", c) # 1
c |= 2
print("Asignación OR a nivel de bits: c |= 2 = ", c)  # 3
c ^= 1
print("Asignación XOR a nivel de bits: c ^= 1 = ", c) # 2
c <<= 1
print("Asignación de desplazamiento a la izquierda: c <<= 1 = ", c) # 4
c >>= 1
print("Asignación de desplazamiento a la derecha: c >>= 1 = ", c) # 2
print(" ")
print("Operadores de Identidad")
print("-----------------------")
d = [1, 2, 3]
e = d
f = [1, 2, 3]
print("d = [1, 2, 3]")
print("e = d")
print("f = [1, 2, 3]")
print("Identidad es: d is e = ", d is e)     # True
print("Identidad no es: d is not f = ", d is not f) # True
print(" ")
print("Operadores de Pertenencia")
print("-------------------------")
print("Pertenencia en: 1 in d = ", 1 in d)   # True
print("Pertenencia no en: 4 not in d = ", 4 not in d) # True