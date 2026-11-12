import math

######################################################
#1. Errores de ejecución
######################################################

print("\n\n=== 1. TypeError (sumar texto y número) ===")
# 1. TypeError: sumar texto y entero
try:
    resultado = "Edad: " + 20
except TypeError as e:
    print("Error:", e)
    print("Solución: 'Edad: ' + str(20)  o  f'Edad: {20}'\n")
    print("TypeError:", e)

print("\n\n=== 2. TypeError (operar matemáticamente con input) ===")
# 2. TypeError: operar con texto devuelto por input
try:
    valor=input("Dame un valor: ")
    resultado = valor * 1.21
except TypeError as e:
    print("Error:", e)
    print("Solución: float(valor) * 1.21\n")
    print("TypeError:", e)

print("\n\n=== 3. ValueError (convertir texto no numérico a int) ===")
# 3. ValueError: texto no numérico a int
try:
    numero = int("veinte")
except ValueError as e:
    print("Error:", e)
    print("Solución: int('20')  o  float('20')\n")
    print("ValueError:", e)

print("\n\n=== 4. ValueError (raíz de número negativo) ===")
# 4. ValueError: raíz de número negativo
try:
    raiz = math.sqrt(-25)
except ValueError as e:
    print("Error:", e)
    print("Solución: validar primero que el número sea >= 0\n")
    print("ValueError:", e)

print("\n\n=== 5. ZeroDivisionError (dividir entre cero) ===")
# 5. ZeroDivisionError: división entre cero
try:
    division = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
    print("Solución: comprobar 'if divisor != 0:' antes de dividir\n")
    print("ZeroDivisionError:", e)

print("\n\n=== 6. NameError (variable no definida o mal escrita) ===")
# 6. NameError: variable no definida
try:
    print(variable_no_creada)
except NameError as e:
    print("Error:", e)
    print("Solución: definir la variable antes de usarla y vigilar mayúsculas/minúsculas\n")
    print("NameError:", e)

print("\n\n=== 7. NameError (usar función sin import) ===")
# 7. NameError: función no definida
try:
    random.randint(1, 10)
except NameError as e:
    print("Error:", e)
    print("Solución: añadir 'import random' o 'from random import randint'\n")
    print("NameError:", e)

print("\n\n=== 8. IndexError (índice fuera de rango) ===")
try:
    texto = "Hola"  # Índices válidos: 0, 1, 2, 3
    letra = texto[4]
except IndexError as e:
    print("Error:", e)
    print("Solución: texto[-1] para el último carácter o comprobar len(texto)\n")
    print("IndexError:", e)

print("\n\n=== 9. AttributeError (método que no pertenece al tipo) ===")
# 8. AttributeError: método inexistente para ese tipo
try:
    numero = 10
    numero.append(5)  # append es de listas, no de enteros
except AttributeError as e:
    print("Error:", e)
    print("Solución: usar métodos compatibles con el tipo de dato\n")
    print("AttributeError:", e)

print("\n\n=== 10. Error Lógico (Precedencia de operadores) ===")
a, b = 10, 20
print("Sin paréntesis  : a + b / 2   =", a + b / 2, "(¡Calcula 10 + 10 = 20.0!)")
print("Con paréntesis  : (a + b) / 2 =", (a + b) / 2, "(Calcula correctamente 15.0)")