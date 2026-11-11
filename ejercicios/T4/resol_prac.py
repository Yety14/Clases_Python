# =====================================================================
# BLOQUE D. CADENAS Y DESCOMPOSICIÓN EN FUNCIONES
# =====================================================================

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

    print("Apariciones de 'p' en 'Programar en Python':", contar_caracter("Programar en Python", "p"))


def solucion_d3():
    frase = "Python es un lenguaje de programación"
    print("Mayúsculas:", frase.upper())
    print("Minúsculas:", frase.lower())
    print("Ordenadas alfabéticamente:", sorted(frase.split(), key=str.lower))


def solucion_d4():
    def es_capicua(palabra):
        limpia = palabra.strip().lower()
        return limpia == limpia[::-1]

    print("¿Radar es capicúa?:", es_capicua("Radar"))
    print("¿Python es capicúa?:", es_capicua("Python"))


def solucion_d5():
    def hora_a_texto(horas, minutos, segundos):
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    print("Hora formateada:", hora_a_texto(9, 5, 3))


def solucion_d6():
    def contar_palabras(texto):
        return len(texto.split())

    def contar_caracter(texto, caracter):
        contador = 0
        for letra in texto:
            if letra.lower() == caracter.lower():
                contador += 1
        return contador

    def contar_palabras_vocal(texto):
        vocales = ("a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú")
        contador = 0
        for palabra in texto.split():
            if palabra and palabra[0].lower() in vocales:
                contador += 1
        return contador

    def resumen_texto(texto, caracter):
        total_p = contar_palabras(texto)
        apariciones = contar_caracter(texto, caracter)
        vocales = contar_palabras_vocal(texto)
        return (f"Palabras: {total_p}, '{caracter}' aparece {apariciones} veces, "
                f"palabras con vocal inicial: {vocales}")

    frase = "El examen práctico evalúa funciones modulares en Python"
    print(resumen_texto(frase, "e"))


def solucion_d7():
    texto = input("Introduce un número entero positivo: ")
    if texto.isdigit():
        print("El doble es:", int(texto) * 2)
    else:
        print("La entrada no contiene únicamente dígitos")


# =====================================================================
# BLOQUE E. FUNCIONES Y RETOS INTEGRADORES DE EXAMEN
# =====================================================================

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

    palabras = ["Python", "es", "un", "lenguaje", "de", "programación", "maravilloso"]
    print("Número de palabras:", contar_palabras(palabras))
    print("Número de caracteres:", contar_caracteres(palabras))
    print("Palabra más larga:", palabra_mas_larga(palabras))
    print("Mayúsculas:", palabras_mayusculas(palabras))
    print("Minúsculas:", palabras_minusculas(palabras))
    print("Ordenadas:", ordenar_palabras(palabras))


def solucion_e2():
    import math

    def area_cuadrado(lado):
        return lado ** 2

    def area_rectangulo(base, altura):
        return base * altura

    def volumen_cubo(arista):
        return arista ** 3

    def volumen_cilindro(radio, altura):
        return math.pi * (radio ** 2) * altura

    figura = input("Selecciona figura (cuadrado, rectangulo, cubo, cilindro): ").strip().lower()

    if figura == "cuadrado":
        lado = float(input("Introduce el lado: "))
        while lado <= 0:
            lado = float(input("Valor incorrecto. Introduce un número positivo: "))
        print("El área del cuadrado es:", area_cuadrado(lado))

    elif figura in ("rectangulo", "rectángulo"):
        base = float(input("Introduce la base: "))
        while base <= 0:
            base = float(input("Valor incorrecto. Introduce base positiva: "))
        altura = float(input("Introduce la altura: "))
        while altura <= 0:
            altura = float(input("Valor incorrecto. Introduce altura positiva: "))
        print("El área del rectángulo es:", area_rectangulo(base, altura))

    elif figura == "cubo":
        arista = float(input("Introduce la arista: "))
        while arista <= 0:
            arista = float(input("Valor incorrecto. Introduce arista positiva: "))
        print("El volumen del cubo es:", volumen_cubo(arista))

    elif figura == "cilindro":
        radio = float(input("Introduce el radio: "))
        while radio <= 0:
            radio = float(input("Valor incorrecto. Introduce radio positivo: "))
        altura = float(input("Introduce la altura: "))
        while altura <= 0:
            altura = float(input("Valor incorrecto. Introduce altura positiva: "))
        print(f"El volumen del cilindro es: {volumen_cilindro(radio, altura):.2f}")

    else:
        print("Opción no válida. Programa terminado.")


def solucion_e3():
    def ordenar_tres(a, b, c):
        if a > b:
            a, b = b, a
        if a > c:
            a, c = c, a
        if b > c:
            b, c = c, b
        return a, b, c

    print("Ordenación de (8, 2, 5):", ordenar_tres(8, 2, 5))


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

    matricula = input("Matrícula del vehículo: ").strip()
    tiempo = float(input("Tiempo empleado en el tramo de 9.3 km (segundos): "))
    while tiempo <= 0:
        tiempo = float(input("Tiempo no válido. Introduce un valor positivo: "))

    vel = velocidad_kmh(9.3, tiempo)
    multa = calcular_multa(vel)

    if multa == 0:
        print(f"El vehículo con matrícula {matricula} circulaba a {vel:.2f} km/h, por lo que no le corresponde sanción.")
    else:
        print(f"El vehículo con matrícula {matricula} circulaba a {vel:.2f} km/h, por lo que le corresponde una sanción de {multa} €.")


def solucion_e5():
    import math

    def aproximar_pi(terminos):
        suma = 0.0
        for i in range(terminos):
            suma += ((-1) ** i) / (2 * i + 1)
        return 4 * suma

    terminos = int(input("Número de términos para aproximar pi: "))
    while terminos <= 0:
        terminos = int(input("Debe ser un entero mayor que cero: "))

    aprox = aproximar_pi(terminos)
    print(f"Aproximación con {terminos} términos: {aprox:.8f}")
    print(f"Valor real de math.pi:               {math.pi:.8f}")
    print(f"Error absoluto:                      {abs(aprox - math.pi):.8f}")


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