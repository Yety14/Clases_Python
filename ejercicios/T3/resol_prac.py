# =====================================================================
# BLOQUE B. CONDICIONALES Y LÓGICA
# =====================================================================

def solucion_b1():
    numero = float(input("Introduce un número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Cero")


def solucion_b2():
    anio = int(input("Introduce un año: "))
    if anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0):
        print("Es bisiesto")
    else:
        print("No es bisiesto")


def solucion_b3():
    nota = float(input("Introduce una nota (0-10): "))
    if nota < 0 or nota > 10:
        print("Nota no válida")
    elif nota < 5:
        print("Suspenso")
    elif nota < 7:
        print("Aprobado")
    elif nota < 9:
        print("Notable")
    else:
        print("Sobresaliente")


def solucion_b4():
    llueve = True
    tengo_paraguas = False
    if not llueve or tengo_paraguas:
        print("SALGO")
    else:
        print("ME QUEDO")


def solucion_b5():
    a = float(input("Lado 1: "))
    b = float(input("Lado 2: "))
    c = float(input("Lado 3: "))
    if a <= 0 or b <= 0 or c <= 0:
        print("Las longitudes deben ser positivas")
    elif a + b <= c or a + c <= b or b + c <= a:
        print("No forman un triángulo")
    elif a == b == c:
        print("Equilátero")
    elif a == b or a == c or b == c:
        print("Isósceles")
    else:
        print("Escaleno")


def solucion_b6():
    edad = int(input("Introduce tu edad (0-120): "))
    while edad < 0 or edad > 120:
        print("Edad no válida")
        edad = int(input("Vuelve a introducir tu edad: "))
    print("Edad válida:", edad)


def solucion_b7():
    opcion = int(input("1. Sumar  2. Restar  3. Multiplicar  4. Dividir: "))
    a, b = 12, 4
    match opcion:
        case 1:
            print(a + b)
        case 2:
            print(a - b)
        case 3:
            print(a * b)
        case 4:
            print(a / b)
        case _:
            print("Opción no válida")


# =====================================================================
# BLOQUE C. BUCLES FOR, WHILE Y RANGE
# =====================================================================

def solucion_c1():
    for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
        print(dia)


def solucion_c2():
    numeros = [10, 20, 30]
    for i in range(len(numeros)):
        print(f"Posición {i} tiene valor {numeros[i]}")


def solucion_c3():
    for numero in range(0, 21, 2):
        print(numero)


def solucion_c4():
    suma = 0
    for numero in range(1, 101):
        suma += numero
    print("Suma total:", suma)


def solucion_c5():
    numero = int(input("¿Qué tabla quieres ver? "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def solucion_c6():
    numero = int(input("Introduce un número entre 1 y 10: "))
    while numero < 1 or numero > 10:
        print("Valor incorrecto")
        numero = int(input("Vuelve a introducirlo: "))
    print("Número válido:", numero)


def solucion_c7():
    for numero in range(1, 11):
        if numero == 7:
            print("¡He encontrado el 7!")
            break


def solucion_c8():
    for numero in range(10):
        if numero == 3 or numero == 7:
            continue
        print(numero)


def solucion_c9():
    n = int(input("Introduce un entero no negativo: "))
    if n < 0:
        print("El número debe ser no negativo")
    else:
        factorial = 1
        contador = 1
        while contador <= n:
            factorial *= contador
            contador += 1
        print(f"{n}! = {factorial}")


def solucion_c10():
    n = int(input("Introduce un entero: "))
    if n < 2:
        es_primo = False
    else:
        es_primo = True
        divisor = 2
        while divisor < n and es_primo:
            if n % divisor == 0:
                es_primo = False
            divisor += 1
    print("Es primo" if es_primo else "No es primo")


def solucion_c11():
    # 1. Validación de edad
    edad = int(input("Introduce tu edad (0-120): "))
    while edad < 0 or edad > 120:
        print("Edad no válida.")
        edad = int(input("Introduce una edad válida (0-120): "))

    # 2. Clasificación de tarifa
    if edad < 12:
        tipo = "Entrada Infantil"
        precio_unitario = 5
    elif edad <= 17:
        tipo = "Entrada Juvenil"
        precio_unitario = 7
    elif edad <= 64:
        tipo = "Entrada General"
        precio_unitario = 10
    else:
        tipo = "Entrada para Adulto Mayor"
        precio_unitario = 6

    print(f"Tipo asignado: {tipo} ({precio_unitario} € cada una)")

    # 3. Número de entradas con validación
    entradas = int(input("¿Cuántas entradas deseas comprar? "))
    while entradas <= 0:
        print("El número de entradas debe ser positivo.")
        entradas = int(input("¿Cuántas entradas deseas comprar? "))

    total = entradas * precio_unitario
    print(f"Importe total a pagar: {total} €")

    # 4. Confirmación de compra con validación
    confirmacion = input("¿Deseas confirmar la compra? (sí/no): ").strip().lower()
    while confirmacion not in ("si", "sí", "no"):
        print("Respuesta no válida.")
        confirmacion = input("¿Deseas confirmar la compra? (sí/no): ").strip().lower()

    if confirmacion in ("si", "sí"):
        print("¡Compra confirmada con éxito! Disfruta de la película.")
    else:
        print("Compra cancelada.")


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