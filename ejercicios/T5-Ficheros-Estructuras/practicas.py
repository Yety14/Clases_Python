# =====================================================================
# BLOQUE F. GESTIÓN DE FICHEROS Y MATRICES (EXÁMENES FINALES)
# =====================================================================

# ---------------------------------------------------------------------
# F.1 Clasificación de pares e impares en ficheros
# (Examen Práctico Final - 1ª Convocatoria 2024/2025, Ejercicio 3)
# Escribe un programa en Python organizado en funciones que realice:
# 1. Crear un archivo llamado 'numeros.txt' que contenga 10 números
#    enteros positivos generados al azar (entre 1 y 100), uno por línea.
# 2. Leer el contenido de 'numeros.txt' y separar los números en pares e impares.
# 3. Guardar los pares en 'pares.txt' y los impares en 'impares.txt'.
# 4. Asegúrate de cerrar correctamente los archivos (o usar 'with').
# ---------------------------------------------------------------------
def solucion_f1():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# F.2 Clasificación de positivos y negativos en ficheros
# (Examen Práctico Final - 2ª Convocatoria 2024/2025, Ejercicio 3)
# Escribe un programa modular que:
# 1. Cree un archivo 'numeros_azar.txt' con 10 números enteros generados
#    al azar en el rango [-100, 100], uno por línea.
# 2. Lea 'numeros_azar.txt' y clasifique los números en positivos (>= 0)
#    y negativos (< 0).
# 3. Guarde los positivos en 'positivos.txt' y los negativos en 'negativos.txt'.
# ---------------------------------------------------------------------
def solucion_f2():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# F.3 Transformación de frases y volcado a fichero
# (Examen Final Convocatoria Enero 2024, Ejercicio 4)
# Realiza un programa que contenga una función que reciba una cadena
# de texto y devuelva la misma frase cambiando la primera y última letra
# de cada palabra a MAYÚSCULAS y el resto a MINÚSCULAS.
# Guarda en el archivo 'salida4.txt' la frase original en la primera línea
# y la frase transformada en la segunda línea.
# Ejemplo entrada: "Hola futuRos inGeniErxs civiles"
# Ejemplo salida:  "HolA FuturoS IngenierxS CivileS"
# ---------------------------------------------------------------------
def solucion_f3():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# F.4 Lista dinámica de números primos (Boletín 3, Ejercicio 1)
# Escribe una función obtener_primos(cantidad) que calcule y devuelva en
# una lista los primeros N números primos (empezando en 2).
# Muestra la lista resultante, el valor del primo más alto y la suma total.
# ---------------------------------------------------------------------
def solucion_f4():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# F.5 Matriz de transporte y kilometraje semanal
# (Examen Final Convocatoria Enero 2024, Ejercicio 2)
# Escribe un programa modular que gestione los kilómetros de una flota:
# 1. Pide el número de camiones N validando que esté en el rango [1, 10].
# 2. Crea e inicializa una matriz de tamaño N x 7 rellena de ceros.
#    (Columna 0 = ID camión 1..N; Columnas 1 a 6 = Km de Lunes a Sábado).
# 3. Rellena los kilómetros de cada camión (validando enteros entre 0 y 8000).
# 4. Define una función promedios_camiones(matriz) que devuelva una lista
#    con la media de kilómetros semanales de cada camión.
# 5. Muestra por pantalla la media de cada camión formateada a 2 decimales.
# 6. Define una función actualizar_camion(matriz, id_camion) que busque
#    al camión por su identificador y solicite actualizar sus km semanales.
# ---------------------------------------------------------------------
def solucion_f5():
    ### CÓDIGO AQUÍ ###
    pass


SOLUCIONES = {
    "F.1": solucion_f1, "F.2": solucion_f2, "F.3": solucion_f3,
    "F.4": solucion_f4, "F.5": solucion_f5
}


if __name__ == "__main__":

    for codigo, funcion in SOLUCIONES.items():
        print(f"\n===== Solución {codigo} =====")
        funcion()