# =====================================================================
# BLOQUE D. CADENAS Y DESCOMPOSICIÓN EN FUNCIONES
# =====================================================================

# ---------------------------------------------------------------------
# D.1 Analizar una frase
# Define una frase. Muestra el número de palabras, el número de caracteres
# sin contar espacios y la palabra más larga. Implementa cada cálculo
# en una función independiente.
# ---------------------------------------------------------------------
def solucion_d1():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# D.2 Contar un carácter
# Escribe una función contar_caracter(texto, caracter) que devuelva cuántas
# veces aparece un carácter en una cadena, sin distinguir mayúsculas y
# minúsculas.
# ---------------------------------------------------------------------
def solucion_d2():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# D.3 Transformar y ordenar palabras
# A partir de la frase 'Python es un lenguaje de programación', muestra
# la frase en mayúsculas, en minúsculas y las palabras ordenadas
# alfabéticamente en una lista.
# ---------------------------------------------------------------------
def solucion_d3():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# D.4 Comprobar si una palabra es capicúa (palíndromo)
# Crea una función es_capicua(palabra) que devuelva True si la palabra se
# lee igual de izquierda a derecha que de derecha a izquierda (sin distinguir
# mayúsculas/minúsculas).
# ---------------------------------------------------------------------
def solucion_d4():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# D.5 Formatear una hora
# Escribe una función hora_a_texto(horas, minutos, segundos) que devuelva una
# cadena con el formato HH:MM:SS, rellenando con ceros a la izquierda.
# Por ejemplo, (9, 5, 3) debe producir '09:05:03'.
# ---------------------------------------------------------------------
def solucion_d5():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# D.6 Crear un resumen de texto (Examen Parcial 2024/2025, Ejercicio 1)
# Define las funciones:
# 1. contar_palabras(texto): devuelve el total de palabras separadas por espacios.
# 2. contar_caracter(texto, caracter): cuenta apariciones de 'caracter'.
# 3. contar_palabras_vocal(texto): cuenta cuántas palabras empiezan por vocal.
# 4. resumen_texto(texto, caracter): utiliza las anteriores y devuelve:
#    "Palabras: X, 'caracter' aparece Y veces, palabras que empiezan por vocal: Z".
# ---------------------------------------------------------------------
def solucion_d6():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# D.7 Comprobar una cadena numérica
# Pide una cadena y comprueba si está formada únicamente por dígitos.
# Si lo está, conviértela a entero y muestra el doble. Si no, informa
# de que no es un número entero positivo escrito como texto.
# ---------------------------------------------------------------------
def solucion_d7():
    ### CÓDIGO AQUÍ ###
    pass


# =====================================================================
# BLOQUE E. FUNCIONES Y RETOS INTEGRADORES DE EXAMEN
# =====================================================================

# ---------------------------------------------------------------------
# E.1 Analizar una lista de palabras (Examen 1ª Convocatoria 2024/2025, Ej. 2)
# Dada la lista:
# palabras = ["Python", "es", "un", "lenguaje", "de", "programación", "maravilloso"]
# Crea una función diferente para:
# 1. Contar el número total de palabras en la lista.
# 2. Sumar el número de caracteres de todas las palabras combinadas.
# 3. Obtener la palabra más larga.
# 4. Devolver una nueva lista con todas en mayúsculas.
# 5. Devolver una nueva lista con todas en minúsculas.
# 6. Devolver la lista ordenada alfabéticamente.
# ---------------------------------------------------------------------
def solucion_e1():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# E.2 Calculadora geométrica modular (Exámenes 2024/2025, Ej. 1)
# Crea funciones modulares para:
# - area_cuadrado(lado)
# - area_rectangulo(base, altura)
# - volumen_cubo(arista)
# - volumen_cilindro(radio, altura)
# Pide qué figura calcular, solicita solo las dimensiones necesarias
# validando que sean estrictamente positivas mediante bucles while, y
# muestra el resultado calculado.
# ---------------------------------------------------------------------
def solucion_e2():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# E.3 Ordenar tres números
# Escribe una función ordenar_tres(a, b, c) que devuelva los tres números
# ordenados de menor a mayor usando únicamente comparaciones e intercambios.
# No utilices sorted ni sort.
# ---------------------------------------------------------------------
def solucion_e3():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# E.4 Velocidad media y multa de radar de tramo (Examen Enero 2024, Ej. 1)
# Un vehículo recorre un tramo de radar fijo de 9.3 km.
# 1. Crea una función velocidad_kmh(distancia_km, tiempo_segundos).
# 2. Crea una función calcular_multa(velocidad):
#    - <= 100 km/h: 0 €
#    - 101 a 130 km/h: 100 €
#    - 131 a 150 km/h: 300 €
#    - 151 a 160 km/h: 400 €
#    - 161 a 170 km/h: 500 €
#    - > 170 km/h: 600 €
# 3. Solicita matrícula, hora de entrada y hora de salida (o tiempo en segundos)
#    validando que el tiempo sea positivo y muestra la sanción correspondiente.
# ---------------------------------------------------------------------
def solucion_e4():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# E.5 Calcular una aproximación de pi (Serie de Gregory-Leibniz)
# Define una función aproximar_pi(terminos) que calcule pi mediante:
# pi = 4 * (1 - 1/3 + 1/5 - 1/7 + ... + (-1)^k / (2k + 1)).
# Compara el resultado con math.pi mostrando el error absoluto.
# ---------------------------------------------------------------------
def solucion_e5():
    ### CÓDIGO AQUÍ ###
    pass


SOLUCIONES = {
    "D.1": solucion_d1, "D.2": solucion_d2, "D.3": solucion_d3,
    "D.4": solucion_d4, "D.5": solucion_d5, "D.6": solucion_d6,
    "D.7": solucion_d7,
    "E.1": solucion_e1, "E.2": solucion_e2, "E.3": solucion_e3,
    "E.4": solucion_e4, "E.5": solucion_e5
}


if __name__ == "__main__":
    for codigo, funcion in SOLUCIONES.items():
        print(f"\n===== Solución {codigo} =====")
        funcion()
