import random
# =====================================================================
# BLOQUE F. GESTIÓN DE FICHEROS Y MATRICES (EXÁMENES FINALES)
# =====================================================================

def solucion_f1():
    # 1. Generar numeros.txt con 10 enteros aleatorios entre 1 y 100
    def generar_archivo(nombre_archivo, cantidad=10):
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            for _ in range(cantidad):
                n = random.randint(1, 100)
                f.write(f"{n}\n")

    # 2. Leer y clasificar en pares e impares
    def clasificar_archivo(origen, f_pares, f_impares):
        pares = []
        impares = []
        with open(origen, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    numero = int(linea)
                    if numero % 2 == 0:
                        pares.append(numero)
                    else:
                        impares.append(numero)

        with open(f_pares, "w", encoding="utf-8") as fp:
            for num in pares:
                fp.write(f"{num}\n")

        with open(f_impares, "w", encoding="utf-8") as fi:
            for num in impares:
                fi.write(f"{num}\n")

        print(f"Pares ({len(pares)}):", pares)
        print(f"Impares ({len(impares)}):", impares)

    generar_archivo("numeros.txt")
    clasificar_archivo("numeros.txt", "pares.txt", "impares.txt")
    print("Archivos 'pares.txt' e 'impares.txt' generados con éxito.")


def solucion_f2():
    # 1. Generar numeros_azar.txt entre -100 y 100
    def generar_archivo_azar(nombre_archivo, cantidad=10):
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            for _ in range(cantidad):
                n = random.randint(-100, 100)
                f.write(f"{n}\n")

    # 2. Separar en positivos y negativos
    def separar_signos(origen, f_pos, f_neg):
        positivos = []
        negativos = []
        with open(origen, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    num = int(linea)
                    if num >= 0:
                        positivos.append(num)
                    else:
                        negativos.append(num)

        with open(f_pos, "w", encoding="utf-8") as fp:
            for n in positivos:
                fp.write(f"{n}\n")

        with open(f_neg, "w", encoding="utf-8") as fn:
            for n in negativos:
                fn.write(f"{n}\n")

        print(f"Positivos ({len(positivos)}):", positivos)
        print(f"Negativos ({len(negativos)}):", negativos)

    generar_archivo_azar("numeros_azar.txt")
    separar_signos("numeros_azar.txt", "positivos.txt", "negativos.txt")
    print("Archivos 'positivos.txt' y 'negativos.txt' creados correctamente.")


def solucion_f3():
    def transformar_palabra(palabra):
        if len(palabra) == 1:
            return palabra.upper()
        # Primera y última letra en mayúscula, el interior en minúscula
        return palabra[0].upper() + palabra[1:-1].lower() + palabra[-1].upper()

    def procesar_frase(frase):
        palabras = frase.split()
        nuevas = [transformar_palabra(p) for p in palabras]
        return " ".join(nuevas)

    frase_original = "Hola futuRos inGeniErxs civiles"
    frase_transformada = procesar_frase(frase_original)

    with open("salida4.txt", "w", encoding="utf-8") as f:
        f.write(frase_original + "\n")
        f.write(frase_transformada + "\n")

    print("Original:    ", frase_original)
    print("Transformada:", frase_transformada)
    print("Guardado en 'salida4.txt'")


def solucion_f4():
    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def obtener_primos(cantidad):
        primos = []
        candidato = 2
        while len(primos) < cantidad:
            if es_primo(candidato):
                primos.append(candidato)
            candidato += 1
        return primos

    n = 25
    lista_primos = obtener_primos(n)
    print(f"Primeros {n} números primos:")
    print(lista_primos)
    print(f"Mayor primo calculado: {max(lista_primos)}")
    print(f"Suma total de los primos: {sum(lista_primos)}")


def solucion_f5():
    # 1. Validación de número de camiones [1-10]
    num_camiones = int(input("Introduce el número de camiones [1-10]: "))
    while num_camiones < 1 or num_camiones > 10:
        num_camiones = int(input("Valor incorrecto. Introduce un valor entre 1 y 10: "))

    # 2. Inicializar matriz de ceros: N filas x 7 columnas
    # Col 0: ID del camión; Cols 1 a 6: Lunes a Sábado
    matriz = [[0 for _ in range(7)] for _ in range(num_camiones)]
    for i in range(num_camiones):
        matriz[i][0] = i + 1

    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

    # 3. Rellenar datos
    print("\n--- Introducción de datos de kilometraje [0 - 8000 km] ---")
    for i in range(num_camiones):
        id_c = matriz[i][0]
        for d in range(6):
            km = int(input(f"Camión {id_c} - Km del {dias[d]}: "))
            while km < 0 or km > 8000:
                km = int(input(f"Valor incorrecto [0-8000]. Camión {id_c} - Km del {dias[d]}: "))
            matriz[i][d + 1] = km

    # 4. Función de promedio semanal
    def promedios_camiones(m):
        promedios = []
        for fila in m:
            suma_dias = sum(fila[1:])
            promedios.append(suma_dias / 6.0)
        return promedios

    # 5. Mostrar medias
    proms = promedios_camiones(matriz)
    print("\n--- Promedios Semanales ---")
    for i in range(num_camiones):
        print(f"El camión {matriz[i][0]} ha recorrido {proms[i]:.2f} Km de promedio semanal")

    # 6. Función para actualizar un camión
    def actualizar_camion(m, id_buscar):
        encontrado = False
        for fila in m:
            if fila[0] == id_buscar:
                encontrado = True
                print(f"\nActualizando datos para el camión {id_buscar}:")
                for d in range(6):
                    nuevo_km = int(input(f"Nuevo km para {dias[d]}: "))
                    while nuevo_km < 0 or nuevo_km > 8000:
                        nuevo_km = int(input(f"Valor [0-8000]. Nuevo km para {dias[d]}: "))
                    fila[d + 1] = nuevo_km
                break
        if not encontrado:
            print(f"El camión con ID {id_buscar} no existe en la flota.")

    # Demostración opcional de actualización
    opc = input("\n¿Deseas actualizar los datos de algún camión? (sí/no): ").strip().lower()
    if opc in ("si", "sí"):
        cid = int(input("ID del camión a actualizar: "))
        actualizar_camion(matriz, cid)
        nuevos_proms = promedios_camiones(matriz)
        print("Promedio actualizado:", f"{nuevos_proms[cid - 1]:.2f} Km" if 1 <= cid <= num_camiones else "")


SOLUCIONES = {
    "F.1": solucion_f1, "F.2": solucion_f2, "F.3": solucion_f3,
    "F.4": solucion_f4, "F.5": solucion_f5
}


if __name__ == "__main__":
    for codigo, funcion in SOLUCIONES.items():
        print(f"\n===== Solución {codigo} =====")
        funcion()
