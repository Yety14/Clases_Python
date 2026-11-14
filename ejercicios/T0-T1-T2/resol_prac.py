# =====================================================================
# BLOQUE A. VARIABLES, TIPOS, OPERADORES Y CÁLCULO TÉCNICO
# SOLUCIONARIO
# =====================================================================

# ---------------------------------------------------------------------
# A.1 Variables y tipos básicos
# Declara las variables edad, altura y nombre con los valores (20, 1.75 y "Ana") 
# respectivamente. Muestra en una sola línea: 
# 'Ana tiene 20 años y mide 1.75 metros'.
# ---------------------------------------------------------------------
def solucion_a1():
    edad = 20
    altura = 1.75
    nombre = "Ana"
    print(f"{nombre} tiene {edad} años y mide {altura} metros")


# ---------------------------------------------------------------------
# A.2 Operaciones aritméticas
# Pide dos números enteros y muestra su suma, resta, producto, división,
# división entera y resto. Comprueba que el segundo número no sea cero
# antes de dividir.
# ---------------------------------------------------------------------
def solucion_a2():
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    print("Suma:", a + b)
    print("Resta:", a - b)
    print("Producto:", a * b)
    if b != 0:
        print("División:", a / b)
        print("División entera:", a // b)
        print("Resto:", a % b)
    else:
        print("No se puede dividir entre cero")


# ---------------------------------------------------------------------
# A.3 Conversión de tipos
# Parte de la cadena texto con valor "100", conviértela a entero, súmale 
# 25 y muestra el resultado como texto. Después, pide al usuario su 
# edad y muestra cuántos años tendrá dentro de 10 años.
# ---------------------------------------------------------------------
def solucion_a3():
    texto = "100"
    numero = int(texto)
    print(str(numero + 25))
    edad = int(input("¿Cuántos años tienes? "))
    print(f"Dentro de 10 años tendrás {edad + 10} años")


# ---------------------------------------------------------------------
# A.4 Porcentajes y formato decimal
# Pide el precio de un producto y el porcentaje de descuento. Calcula
# el precio final y muéstralo con exactamente dos decimales.
# ---------------------------------------------------------------------
def solucion_a4():
    precio = float(input("Precio original: "))
    descuento = float(input("Descuento (%): "))
    precio_final = precio * (1 - descuento / 100)
    print(f"El precio final es {precio_final:.2f} euros")


# ---------------------------------------------------------------------
# A.5 Conversión de segundos
# Pide una cantidad total de segundos y conviértela en horas, minutos y
# segundos. Por ejemplo, 3671 segundos son 1 hora, 1 minuto y 11 segundos.
# ---------------------------------------------------------------------
def solucion_a5():
    total = int(input("Introduce los segundos: "))
    horas = total // 3600
    resto = total % 3600
    minutos = resto // 60
    segundos = resto % 60
    print(f"{horas} horas, {minutos} minutos y {segundos} segundos")


# ---------------------------------------------------------------------
# A.6 Funciones matemáticas
# Pide el radio de un círculo y calcula su longitud (2*pi*r) y su área 
# (pi*r^2). Muestra ambos resultados con dos decimales usando math.pi.
# ---------------------------------------------------------------------
def solucion_a6():
    import math
    radio = float(input("Radio del círculo: "))
    print(f"Longitud: {2 * math.pi * radio:.2f}")
    print(f"Área: {math.pi * radio ** 2:.2f}")


# ---------------------------------------------------------------------
# A.7 Números aleatorios
# Genera un número entero aleatorio entre 1 y 100. Después, elige al azar
# un color de la lista ['rojo', 'verde', 'azul'] y muestra ambos resultados.
# ---------------------------------------------------------------------
def solucion_a7():
    import random
    print("Número:", random.randint(1, 100))
    print("Color:", random.choice(["rojo", "verde", "azul"]))


# ---------------------------------------------------------------------
# A.8 Ecuación de segundo grado
# Pide los coeficientes a, b y c de una ecuación ax^2 + bx + c = 0, con a!=0.
# Calcula el discriminante (d = b^2 - 4ac). Si d >= 0, calcula y muestra
# las dos soluciones reales usando math.sqrt. Si d < 0, muestra que no
# existen raíces reales.
# ---------------------------------------------------------------------
def solucion_a8():
    import math
    a = float(input("Coeficiente a: "))
    b = float(input("Coeficiente b: "))
    c = float(input("Coeficiente c: "))
    if a == 0:
        print("a no puede ser cero (no es una ecuación de segundo grado)")
        return
    d = b ** 2 - 4 * a * c
    if d >= 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"Soluciones: x1 = {x1:.2f}, x2 = {x2:.2f}")
    else:
        print("No existen raíces reales")


# ---------------------------------------------------------------------
# A.9 Canal trapezoidal de ingeniería civil
# Pide el ancho inferior (b), el ancho superior (B) y la altura (h) de 
# un canal trapezoidal. Calcula y muestra con dos decimales:
# - Área hidráulica: ((B + b) / 2) * h
# - Perímetro mojado: b + 2 * math.sqrt(((B - b) / 2)**2 + h**2)
# ---------------------------------------------------------------------
def solucion_a9():
    import math
    b = float(input("Ancho inferior (b): "))
    B = float(input("Ancho superior (B): "))
    h = float(input("Altura (h): "))
    area = ((B + b) / 2) * h
    perimetro = b + 2 * math.sqrt(((B - b) / 2) ** 2 + h ** 2)
    print(f"Área hidráulica: {area:.2f}")
    print(f"Perímetro mojado: {perimetro:.2f}")


# ---------------------------------------------------------------------
# A.10 Salto de reloj
# Pide la hora actual de un reloj (horas, minutos y segundos) y una
# cantidad de segundos adicionales 'x'. Calcula y muestra qué hora
# marcará el reloj dentro de esos segundos en formato HH:MM:SS
# teniendo en cuenta el cambio de día (ciclo de 24 horas).
# ---------------------------------------------------------------------
def solucion_a10():
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))
    x = int(input("Segundos adicionales (x): "))
    total = (horas * 3600 + minutos * 60 + segundos + x) % 86400
    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60
    print(f"{h:02d}:{m:02d}:{s:02d}")


SOLUCIONES = {
    "A.1": solucion_a1, "A.2": solucion_a2, "A.3": solucion_a3,
    "A.4": solucion_a4, "A.5": solucion_a5, "A.6": solucion_a6,
    "A.7": solucion_a7, "A.8": solucion_a8, "A.9": solucion_a9,
    "A.10": solucion_a10
}


if __name__ == "__main__":
    for codigo, funcion in SOLUCIONES.items():
        print(f"\n===== Solución {codigo} =====")
        funcion()