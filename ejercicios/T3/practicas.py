# =====================================================================
# BLOQUE B. CONDICIONALES Y LÓGICA (if/elif/else y match/case)
# =====================================================================

# ---------------------------------------------------------------------
# B.1 Clasificar un número
# Pide un número y muestra si es positivo, negativo o igual a cero.
# ---------------------------------------------------------------------
def solucion_b1():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# B.2 Año bisiesto
# Pide un año e indica si es bisiesto. Un año es bisiesto si es divisible
# por 400, o si es divisible por 4 pero no por 100.
# ---------------------------------------------------------------------
def solucion_b2():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# B.3 Validar una nota
# Pide una nota entre 0 y 10. Si está fuera del intervalo, muestra un
# mensaje de error. En caso contrario, indica si está suspenso (<5),
# aprobado (5 a <7), notable (7 a <9) o sobresaliente (>=9).
# ---------------------------------------------------------------------
def solucion_b3():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# B.4 Decidir si salir a la calle
# Define las variables llueve y tengo_paraguas. Se sale si no llueve o si
# llueve y se tiene paraguas. Muestra 'SALGO' o 'ME QUEDO'.
# ---------------------------------------------------------------------
def solucion_b4():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# B.5 Tipo de triángulo
# Pide las longitudes de tres lados. Comprueba primero que sean positivas
# y que puedan formar un triángulo (la suma de dos lados cualesquiera
# debe ser estrictamente mayor que el tercero). Si lo forman, indica si
# es equilátero, isósceles o escaleno.
# ---------------------------------------------------------------------
def solucion_b5():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# B.6 Validar una edad
# Solicita una edad y repite la petición mientras no sea un entero entre
# 0 y 120, ambos incluidos. Cuando sea válida, muestra la edad aceptada.
# ---------------------------------------------------------------------
def solucion_b6():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# B.7 Menú con match/case
# Pide un número del 1 al 4 y muestra una operación: 1 sumar, 2 restar,
# 3 multiplicar y 4 dividir. Para cualquier otro valor, 'Opción no válida'.
# ---------------------------------------------------------------------
def solucion_b7():
    ### CÓDIGO AQUÍ ###
    pass


# =====================================================================
# BLOQUE C. BUCLES FOR, WHILE Y RANGE
# =====================================================================

# ---------------------------------------------------------------------
# C.1 Recorrer una secuencia
# Recorre la lista ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
# e imprime cada día en una línea diferente.
# ---------------------------------------------------------------------
def solucion_c1():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# C.2 Recorrer con índices
# Dada la lista [10, 20, 30], muestra para cada elemento su posición y su
# valor con el formato 'Posición X tiene valor Y'.
# ---------------------------------------------------------------------
def solucion_c2():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# C.3 Múltiplos con range
# Muestra los números pares entre 0 y 20, ambos incluidos, usando el
# tercer argumento de range para avanzar de dos en dos.
# ---------------------------------------------------------------------
def solucion_c3():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# C.4 Suma mediante un acumulador
# Calcula la suma de todos los números enteros del 1 al 100 y muestra
# el resultado al terminar el bucle.
# ---------------------------------------------------------------------
def solucion_c4():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# C.5 Tabla de multiplicar
# Pide un número entero y muestra su tabla de multiplicar del 1 al 10.
# ---------------------------------------------------------------------
def solucion_c5():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# C.6 Validar una entrada con while
# Pide un número entero entre 1 y 10. Mientras el valor esté fuera de ese
# intervalo, vuelve a pedirlo. Cuando sea válido, muestra el número.
# ---------------------------------------------------------------------
def solucion_c6():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# C.7 Búsqueda con break
# Recorre los números del 1 al 10. Cuando encuentres el 7, muestra un
# mensaje y termina inmediatamente el bucle mediante break.
# ---------------------------------------------------------------------
def solucion_c7():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# C.8 Saltar iteraciones con continue
# Recorre los números del 0 al 9 e imprime todos excepto el 3 y el 7.
# Utiliza continue para saltar esas iteraciones.
# ---------------------------------------------------------------------
def solucion_c8():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# C.9 Calcular un factorial
# Pide un entero no negativo y calcula su factorial. Recuerda que 0! = 1.
# Resuélvelo con un bucle, sin usar math.factorial.
# ---------------------------------------------------------------------
def solucion_c9():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# C.10 Números primos
# Pide un entero y determina si es primo. Un número primo es mayor que 1
# y solo tiene dos divisores: 1 y él mismo.
# ---------------------------------------------------------------------
def solucion_c10():
    ### CÓDIGO AQUÍ ###
    pass


# ---------------------------------------------------------------------
# C.11 Reto de Examen: Gestión de entradas de cine (Parcial 2024/2025)
# 1. Pide la edad validando que esté entre 0 y 120 con un bucle while.
# 2. Clasifica la tarifa:
#    - < 12 años: Infantil (5 €)
#    - 13 a 17 años: Juvenil (7 €)
#    - 18 a 64 años: General (10 €)
#    - >= 65 años: Adulto Mayor (6 €)
# 3. Pide el número de entradas deseado validando que sea > 0 con while.
# 4. Muestra el importe total a pagar.
# 5. Pregunta si confirma la compra ('sí' o 'no'), repitiendo la pregunta
#    con while si la respuesta no es ninguna de las dos opciones.
# ---------------------------------------------------------------------
def solucion_c11():
    ### CÓDIGO AQUÍ ###
    pass


SOLUCIONES = {
    "B.1": solucion_b1, "B.2": solucion_b2, "B.3": solucion_b3,
    "B.4": solucion_b4, "B.5": solucion_b5, "B.6": solucion_b6,
    "B.7": solucion_b7,
    "C.1": solucion_c1, "C.2": solucion_c2, "C.3": solucion_c3,
    "C.4": solucion_c4, "C.5": solucion_c5, "C.6": solucion_c6,
    "C.7": solucion_c7, "C.8": solucion_c8, "C.9": solucion_c9,
    "C.10": solucion_c10, "C.11": solucion_c11
}


if __name__ == "__main__":
    for codigo, funcion in SOLUCIONES.items():
        print(f"\n===== Solución {codigo} =====")
        funcion()
