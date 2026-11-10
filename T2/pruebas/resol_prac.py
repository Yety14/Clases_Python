
# =====================================================================
# ANEXO. SOLUCIONES FUNCIONALES
# =====================================================================

def solucion_a1():
    nombre = "Ana"
    edad = 20
    altura = 1.75
    print(f"{nombre} tiene {edad} años y mide {altura} metros")


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


def solucion_a3():
    texto = "100"
    numero = int(texto)
    print(str(numero + 25))
    edad = int(input("¿Cuántos años tienes? "))
    print(f"Dentro de 10 años tendrás {edad + 10} años")


def solucion_a4():
    precio = float(input("Precio original: "))
    descuento = float(input("Descuento (%): "))
    print(f"El precio final es {precio * (1 - descuento / 100):.2f} euros")


def solucion_a5():
    total = int(input("Introduce los segundos: "))
    horas = total // 3600
    resto = total % 3600
    minutos = resto // 60
    segundos = resto % 60
    print(f"{horas} horas, {minutos} minutos y {segundos} segundos")


def solucion_a6():
    import math
    radio = float(input("Radio del círculo: "))
    print(f"Longitud: {2 * math.pi * radio:.2f}")
    print(f"Área: {math.pi * radio ** 2:.2f}")


def solucion_a7():
    import random
    print("Número:", random.randint(1, 100))
    print("Color:", random.choice(["rojo", "verde", "azul"]))


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


def solucion_d1():
    def contar_palabras(texto):
        return len(texto.split())

    def contar_caracteres_sin_espacios(texto):
        return len(texto.replace(" ", ""))

    def palabra_mas_larga(texto):
        palabras = texto.split()
        return max(palabras, key=len) if palabras else ""

    frase = "Python es un lenguaje de programación maravilloso"
    print("Número de palabras:", contar_palabras(frase))
    print("Caracteres sin espacios:", contar_caracteres_sin_espacios(frase))
    print("Palabra más larga:", palabra_mas_larga(frase))


def solucion_d2():
    def contar_caracter(texto, caracter):
        contador = 0
        for letra in texto:
            if letra.lower() == caracter.lower():
                contador += 1
        return contador

    print(contar_caracter("Programar en Python", "p"))


def solucion_d3():
    frase = "Python es un lenguaje de programación"
    print(frase.upper())
    print(frase.lower())
    print(sorted(frase.split(), key=str.lower))


def solucion_d4():
    def es_capicua(palabra):
        palabra = palabra.lower()
        return palabra == palabra[::-1]

    print(es_capicua("Radar"))
    print(es_capicua("Python"))


def solucion_d5():
    def hora_a_texto(horas, minutos, segundos):
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    print(hora_a_texto(9, 5, 3))


def solucion_d6():
    def contar_palabras(texto):
        return len(texto.split())

    def contar_caracter(texto, caracter):
        contador = 0
        for letra in texto:
            if letra == caracter:
                contador += 1
        return contador

    def resumen_texto(texto, caracter):
        return (f"Palabras: {contar_palabras(texto)}, "
                f"'{caracter}' aparece {contar_caracter(texto, caracter)} veces")

    print(resumen_texto("Python es un lenguaje", "e"))


def solucion_d7():
    texto = input("Introduce un número entero positivo: ")
    if texto.isdigit():
        print("El doble es:", int(texto) * 2)
    else:
        print("La entrada no contiene únicamente dígitos")


def solucion_e1():
    def contar_palabras(lista):
        return len(lista)

    def contar_caracteres(lista):
        total = 0
        for palabra in lista:
            total += len(palabra)
        return total

    def palabra_mas_larga(lista):
        return max(lista, key=len)

    def palabras_mayusculas(lista):
        return [palabra.upper() for palabra in lista]

    def palabras_minusculas(lista):
        return [palabra.lower() for palabra in lista]

    def ordenar_palabras(lista):
        return sorted(lista, key=str.lower)

    palabras = ["Python", "es", "un", "lenguaje", "de", "programación"]
    print("Número de palabras:", contar_palabras(palabras))
    print("Número de caracteres:", contar_caracteres(palabras))
    print("Palabra más larga:", palabra_mas_larga(palabras))
    print("Mayúsculas:", palabras_mayusculas(palabras))
    print("Minúsculas:", palabras_minusculas(palabras))
    print("Ordenadas:", ordenar_palabras(palabras))


def solucion_e2():
    def area_cuadrado(lado):
        return lado ** 2

    def area_rectangulo(base, altura):
        return base * altura

    figura = input("¿Cuadrado o rectángulo? ").lower()
    if figura == "cuadrado":
        lado = float(input("Lado: "))
        if lado > 0:
            print("Área:", area_cuadrado(lado))
        else:
            print("El lado debe ser positivo")
    elif figura in ("rectangulo", "rectángulo"):
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        if base > 0 and altura > 0:
            print("Área:", area_rectangulo(base, altura))
        else:
            print("Las dimensiones deben ser positivas")
    else:
        print("Figura no válida")


def solucion_e3():
    def ordenar_tres(a, b, c):
        if a > b:
            a, b = b, a
        if a > c:
            a, c = c, a
        if b > c:
            b, c = c, b
        return a, b, c

    print(ordenar_tres(8, 2, 5))


def solucion_e4():
    def velocidad_kmh(distancia_km, tiempo_segundos):
        return distancia_km / (tiempo_segundos / 3600)

    def calcular_multa(velocidad):
        if velocidad <= 100:
            return 0
        elif velocidad <= 130:
            return 100
        elif velocidad <= 150:
            return 300
        elif velocidad <= 160:
            return 400
        elif velocidad <= 170:
            return 500
        else:
            return 600

    tiempo = float(input("Tiempo empleado (segundos): "))
    if tiempo <= 0:
        print("El tiempo debe ser positivo")
    else:
        velocidad = velocidad_kmh(9.3, tiempo)
        multa = calcular_multa(velocidad)
        print(f"Velocidad media: {velocidad:.2f} km/h")
        if multa == 0:
            print("No corresponde sanción")
        else:
            print(f"Importe de la multa: {multa} euros")


def solucion_e5():
    import math
    terminos = int(input("Número de términos: "))
    if terminos <= 0:
        print("Debe introducirse al menos un término")
    else:
        suma = 0
        for i in range(terminos):
            suma += (-1) ** i / (2 * i + 1)
        aproximacion = 4 * suma
        print(f"Aproximación: {aproximacion:.6f}")
        print(f"Valor de math.pi: {math.pi:.6f}")


SOLUCIONES = {
    "A.1": solucion_a1, "A.2": solucion_a2, "A.3": solucion_a3,
    "A.4": solucion_a4, "A.5": solucion_a5, "A.6": solucion_a6,
    "A.7": solucion_a7, "B.1": solucion_b1, "B.2": solucion_b2,
    "B.3": solucion_b3, "B.4": solucion_b4, "B.5": solucion_b5,
    "B.6": solucion_b6, "B.7": solucion_b7, "C.1": solucion_c1,
    "C.2": solucion_c2, "C.3": solucion_c3, "C.4": solucion_c4,
    "C.5": solucion_c5, "C.6": solucion_c6, "C.7": solucion_c7,
    "C.8": solucion_c8, "C.9": solucion_c9, "C.10": solucion_c10,
    "D.1": solucion_d1, "D.2": solucion_d2, "D.3": solucion_d3,
    "D.4": solucion_d4, "D.5": solucion_d5, "D.6": solucion_d6,
    "D.7": solucion_d7, "E.1": solucion_e1, "E.2": solucion_e2,
    "E.3": solucion_e3, "E.4": solucion_e4, "E.5": solucion_e5,
}


if __name__ == "__main__":
    if MOSTRAR_SOLUCIONES:
        for codigo, funcion in SOLUCIONES.items():
            print(f"\n===== Solución {codigo} =====")
            funcion()