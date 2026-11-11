
MOSTRAR_SOLUCIONES = True
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
    match opcion:
        case 1:
            print("Suma")
        case 2:
            print("Resta")
        case 3:
            print("Multiplicación")
        case 4:
            print("Division")
        case _:
            print("Opción no válida")


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


SOLUCIONES = {
    "A.1": solucion_a1, "A.2": solucion_a2, "A.3": solucion_a3,
    "A.4": solucion_a4, "A.5": solucion_a5, "A.6": solucion_a6,
    "A.7": solucion_a7, "B.1": solucion_b1, "B.2": solucion_b2,
    "B.3": solucion_b3, "B.4": solucion_b4, "B.5": solucion_b5,
    "B.6": solucion_b6, "B.7": solucion_b7, "D.1": solucion_d1,
    "D.2": solucion_d2, "D.3": solucion_d3, "D.4": solucion_d4,
    "D.5": solucion_d5, "D.6": solucion_d6, "D.7": solucion_d7
}


if __name__ == "__main__":
    if MOSTRAR_SOLUCIONES:
        for codigo, funcion in SOLUCIONES.items():
            print(f"\n===== Solución {codigo} =====")
            funcion()