# =====================================================================
# BLOQUE A. VARIABLES, TIPOS, OPERADORES Y CÁLCULO TÉCNICO
# =====================================================================

# ---------------------------------------------------------------------
# A.1 Variables y tipos básicos
# Declara las variables edad, altura y nombre con los valores (20, 1.75 y "Ana") 
# respectivamente. Muestra en una sola línea: 
# 'Ana tiene 20 años y mide 1.75 metros'.
# ---------------------------------------------------------------------
def solucion_a1():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# A.2 Operaciones aritméticas
# Pide dos números enteros y muestra su suma, resta, producto, división,
# división entera y resto. Comprueba que el segundo número no sea cero
# antes de dividir.
# ---------------------------------------------------------------------
def solucion_a2():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# A.3 Conversión de tipos
# Parte de la cadena texto con valor "100", conviértela a entero, súmale 
# 25 y muestra el resultado como texto. Después, pide al usuario su 
# edad y muestra cuántos años tendrá dentro de 10 años.
# ---------------------------------------------------------------------
def solucion_a3():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# A.4 Porcentajes y formato decimal
# Pide el precio de un producto y el porcentaje de descuento. Calcula
# el precio final y muéstralo con exactamente dos decimales.
# ---------------------------------------------------------------------
def solucion_a4():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# A.5 Conversión de segundos
# Pide una cantidad total de segundos y conviértela en horas, minutos y
# segundos. Por ejemplo, 3671 segundos son 1 hora, 1 minuto y 11 segundos.
# ---------------------------------------------------------------------
def solucion_a5():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# A.6 Funciones matemáticas
# Pide el radio de un círculo y calcula su longitud (2*pi*r) y su área 
# (pi*r^2). Muestra ambos resultados con dos decimales usando math.pi.
# ---------------------------------------------------------------------
def solucion_a6():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# A.7 Números aleatorios
# Genera un número entero aleatorio entre 1 y 100. Después, elige al azar
# un color de la lista ['rojo', 'verde', 'azul'] y muestra ambos resultados.
# ---------------------------------------------------------------------
def solucion_a7():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# A.8 Ecuación de segundo grado (Boletín 1, Ej. 4)
# Pide los coeficientes a, b y c de una ecuación ax^2 + bx + c = 0.
# Calcula el discriminante (d = b^2 - 4ac). Si d >= 0, calcula y muestra
# las dos soluciones reales usando math.sqrt. Si d < 0, muestra que no
# existen raíces reales.
# ---------------------------------------------------------------------
def solucion_a8():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# A.9 Canal trapezoidal de ingeniería civil (Boletín 1, Ej. 11)
# Pide el ancho inferior (b), el ancho superior (B) y la altura (h) de 
# un canal trapezoidal. Calcula y muestra con dos decimales:
# - Área hidráulica: ((B + b) / 2) * h
# - Perímetro mojado: b + 2 * math.sqrt(((B - b) / 2)**2 + h**2)
# ---------------------------------------------------------------------
def solucion_a9():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# A.10 Salto de reloj (Boletín 2, Ej. 1)
# Pide la hora actual de un reloj (horas, minutos y segundos) y una
# cantidad de segundos adicionales 'x'. Calcula y muestra qué hora
# marcará el reloj dentro de esos segundos en formato HH:MM:SS
# teniendo en cuenta el cambio de día (ciclo de 24 horas).
# ---------------------------------------------------------------------
def solucion_a10():
    ### CÓDIGO AQUÍ ###
    pass


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
