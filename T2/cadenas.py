"""
MANIPULACIÓN DE CADENAS EN PYTHON - PARTE 2 (lo que NO estaba en cadenas_examen.py)
Mismo estilo: cada bloque es independiente. Ejecuta el archivo para ver los resultados.
Incluye validación de DNI (Enero 24, ej. 1a) y ejercicios típicos de examen.
"""

# =====================================================================
# 1. MÁS MÉTODOS DE BÚSQUEDA
# =====================================================================
def mas_busqueda():
    t = "el perro y el gato y el pez"
    print(t.count("el"))                     # 3  (cuántas veces aparece una subcadena)
    print(t.rfind("el"))                     # 21 (find pero empezando por la derecha)
    print(t[21],t[22])
    print(t.find("el", 5))                   # 11 (2º argumento: posición desde la que buscar)
    print(t.index("gato"))                   # 14 (como find, pero si no existe da ValueError)
    print(t.startswith("el"))                # True
    print(t.endswith("pez"))                 # True
    print(t.startswith(("el", "la")))        # True (con tupla: vale cualquiera de las dos)


# =====================================================================
# 2. split, join Y VARIANTES
# =====================================================================
def mas_split_y_join():
    print("a,b,    c".split(","))                # ['a', 'b', 'c']  (split con separador)
    print("a,b,c,d".split(",", 2))           # ['a', 'b', 'c,d'] (2º argumento: nº máx. de cortes)
    print("a  b   c".split())                # ['a', 'b', 'c']  (sin argumento agrupa espacios)
    print("a  b".split(" "))                 # ['a', '', 'b']   (OJO: con " " sí salen vacíos)
    print("l1\nl2\nl3".splitlines())         # ['l1', 'l2', 'l3'] (separa por saltos de línea)
    print("-".join(["a", "b", "c"]))         # 'a-b-c' (join se llama sobre el SEPARADOR)
    print("".join(["h", "o", "l", "a"]))     # 'hola'  (separador vacío: pega sin nada)
    print("clave=valor".partition("="))      # ('clave', '=', 'valor') (corta en el 1er '=')


# =====================================================================
# 3. LIMPIAR Y ALINEAR
# =====================================================================
def limpiar_y_alinear():
    print("  hola  ".lstrip() + "|")         # 'hola  |' (solo quita a la izquierda)
    print("  hola  ".rstrip() + "|")         # '  hola|' (solo quita a la derecha)
    print("***hola***".strip("*"))           # 'hola' (strip con los caracteres a quitar)
    print("hOLA mUNDO".capitalize())         # 'Hola mundo' (1ª en mayúscula, resto minúscula)
    print("Hola Mundo".swapcase())           # 'hOLA mUNDO' (invierte mayúsculas/minúsculas)
    print("hola".center(10, "-"))            # '---hola---'
    print("hola".ljust(8, ".") + "|")        # 'hola....|' (rellena a la derecha)
    print("hola".rjust(8, ".") + "|")        # '....hola|' (rellena a la izquierda)
    print("7".zfill(3))                      # '007' (rellena con ceros, útil para horas 09:05)
    print("ab" * 3 + "-" + "c")              # 'ababab-c' (repetición y concatenación)


# =====================================================================
# 4. MÁS PREGUNTAS DE TIPO (is...)
# =====================================================================
def mas_comprobaciones():
    print("abc123".isalnum())                # True  (solo letras y/o números)
    print("abc 123".isalnum())               # False (el espacio no cuenta)
    print("Hola Mundo".istitle())            # True  (cada palabra empieza en mayúscula)
    print("12.5".isdigit())                  # False (el punto no es dígito)
    print("-5".isdigit())                    # False (el signo tampoco: ojo al validar números)
    print("".isalpha())                      # False (la cadena vacía siempre da False)


# =====================================================================
# 5. RECORRER CADENAS
# =====================================================================
def recorrer():
    t = "hola"
    for i, c in enumerate(t):                # enumerate da posición y carácter a la vez
        print(i, c)
    for c in reversed(t):                    # recorre de derecha a izquierda
        print(c, end="")
    print()
    print(max("hola"), min("hola"))          # 'o' 'a' (compara con ord, como en el Tema 2)
    print(sorted("hola"))                    # ['a', 'h', 'l', 'o'] (devuelve una LISTA)
    print("".join(sorted("hola")))           # 'ahlo' (para volver a tener cadena)
    print(sorted("Hola Mundo", key=str.lower))   # key=str.lower ordena sin distinguir may/min


# =====================================================================
# 6. CONTAR FRECUENCIAS (diccionarios)
# =====================================================================
def frecuencias(texto):
    """Devuelve un diccionario {carácter: veces}. Ej: 'hola' -> {'h':1,'o':1,'l':1,'a':1}"""
    cuenta = {}
    for c in texto:
        if c in cuenta:
            cuenta[c] += 1
        else:
            cuenta[c] = 1
    return cuenta                            # forma corta: cuenta[c] = cuenta.get(c, 0) + 1


def caracter_mas_repetido(texto):
    cuenta = frecuencias(texto.replace(" ", ""))
    mas = ""
    for c in cuenta:
        if mas == "" or cuenta[c] > cuenta[mas]:
            mas = c
    return mas


def palabras_repetidas(texto):
    """Palabras que aparecen más de una vez (sin distinguir mayúsculas)."""
    cuenta = {}
    for p in texto.lower().split():
        cuenta[p] = cuenta.get(p, 0) + 1
    return [p for p in cuenta if cuenta[p] > 1]


# =====================================================================
# 7. ELIMINAR Y FILTRAR
# =====================================================================
def quitar_vocales(texto):
    resultado = ""
    for c in texto:
        if c.lower() not in "aeiouáéíóú":
            resultado += c
    return resultado


def quitar_repetidos(texto):
    """'banana' -> 'ban' (deja la primera aparición de cada carácter, respeta el orden)."""
    resultado = ""
    for c in texto:
        if c not in resultado:
            resultado += c
    return resultado


def solo_letras(texto):
    return "".join(c for c in texto if c.isalpha())


def solo_digitos(texto):
    return "".join(c for c in texto if c.isdigit())


def quitar_signos(texto, signos=".,;:!?¡¿"):
    for s in signos:
        texto = texto.replace(s, "")
    return texto


def sustituir_varios(texto, tabla):
    """Sustituye varios caracteres a la vez con un diccionario. Ej: {'a':'4','e':'3'}"""
    resultado = ""
    for c in texto:
        resultado += tabla.get(c, c)         # get(c, c): si no está en la tabla, deja c
    return resultado


def sustituir_con_translate(texto):
    tabla = str.maketrans("aeiou", "12345")  # maketrans empareja posición a posición
    return texto.translate(tabla)            # 'hola' -> 'h4l1'


# =====================================================================
# 8. COMPARAR CADENAS
# =====================================================================
def son_anagramas(a, b):
    """'Roma' y 'amor' -> True (mismas letras, distinto orden)."""
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    return sorted(a) == sorted(b)


def comparar():
    print("hola" == "Hola")                  # False (distingue mayúsculas)
    print("hola".lower() == "Hola".lower())  # True
    print("abajo" < "arriba")                # True  (carácter a carácter, como en el Tema 2)
    print("10" < "9")                        # True  (¡se comparan como texto, no como número!)
    print(int("10") < int("9"))              # False (hay que convertir antes)


# =====================================================================
# 9. VALIDACIONES (Enero 24, ej. 1a: validar DNI; matrículas)
# =====================================================================
def dni_valido(dni):
    """8 dígitos + letra correcta (la letra sale de número % 23)."""
    dni = dni.strip().upper()
    if len(dni) != 9:
        return False
    if not dni[:8].isdigit():
        return False
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return dni[8] == letras[int(dni[:8]) % 23]


def matricula_valida(m):
    """Formato actual: 4 dígitos + 3 letras. Ej: 1782MBT."""
    m = m.strip().upper()
    return len(m) == 7 and m[:4].isdigit() and m[4:].isalpha()


def pedir_dni():
    """Repite hasta que sea válido (patrón típico de los exámenes)."""
    dni = input("DNI: ")
    while not dni_valido(dni):
        dni = input("DNI incorrecto, vuelve a escribirlo: ")
    return dni


def es_entero_texto(t):
    """Acepta '-5' y '12' (isdigit solo no acepta el signo)."""
    if t.startswith("-"):
        t = t[1:]
    return t.isdigit()


# =====================================================================
# 10. EJERCICIOS TÍPICOS DE EXAMEN
# =====================================================================
def mayuscula_tras_punto(texto):
    """'hola. que tal. bien' -> 'Hola. Que tal. Bien'"""
    resultado = ""
    poner_mayuscula = True
    for c in texto:
        if poner_mayuscula and c.isalpha():
            resultado += c.upper()
            poner_mayuscula = False
        else:
            resultado += c
        if c in ".!?":
            poner_mayuscula = True
    return resultado


def comprimir(texto):
    """Compresión RLE: 'aaabccdddd' -> 'a3b1c2d4'"""
    if texto == "":
        return ""
    resultado = ""
    actual = texto[0]
    veces = 1
    for c in texto[1:]:
        if c == actual:
            veces += 1
        else:
            resultado += actual + str(veces)
            actual = c
            veces = 1
    resultado += actual + str(veces)         # no olvidar el último grupo
    return resultado


def acronimo(frase):
    """'Escuela Politécnica Superior' -> 'EPS'"""
    return "".join(p[0].upper() for p in frase.split())


def alternar_mayusculas(texto):
    """'hola mundo' -> 'HoLa mUnDo' (alterna por posición; el espacio también cuenta como posición)."""
    resultado = ""
    for i in range(len(texto)):
        if i % 2 == 0:
            resultado += texto[i].upper()
        else:
            resultado += texto[i].lower()
    return resultado


def decimal_a_binario_texto(n):
    """Boletín 3 ej. 3, versión con cadenas. 10 -> '1010'"""
    if n == 0:
        return "0"
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario       # se añade por la IZQUIERDA
        n //= 2
    return binario                           # comprobación: bin(10) -> '0b1010'


def hora_a_texto(h, m, s):
    """9, 5, 3 -> '09:05:03' (Enero 24, ej. 1b)"""
    return f"{h:02d}:{m:02d}:{s:02d}"        # 02d: mínimo 2 caracteres rellenando con ceros


def texto_a_hora(t):
    """'09:05:03' -> (9, 5, 3)"""
    partes = t.split(":")
    return int(partes[0]), int(partes[1]), int(partes[2])


# =====================================================================
# 11. CARACTERES ESPECIALES Y OTROS DETALLES
# =====================================================================
def especiales():
    print("Linea1\nLinea2")                  # \n salto de línea
    print("Col1\tCol2")                      # \t tabulador
    print("Dijo \"hola\"")                   # \" comilla dentro de comillas
    print('Dijo "hola"')                     # otra opción: alternar tipo de comillas
    print("C:\\carpeta\\archivo")            # \\ para escribir una barra
    print(r"C:\carpeta\archivo")             # r"..." (cadena cruda) no interpreta las barras
    print("""Varias
líneas""")                                   # triple comilla: texto en varias líneas
    x = 5
    print(f"{x=}")                           # 'x=5' (f-string que muestra nombre y valor)
    print(f"{x:>5}|{x:<5}|{x:^5}|")          # '    5|5    |  5  |' (derecha, izquierda, centro)
    print(f"{1234567:,}")                    # '1,234,567' (separador de miles)
    print(f"{0.256:.1%}")                    # '25.6%' (porcentaje)


# =====================================================================
# PRUEBAS
# =====================================================================
if __name__ == "__main__":
    print("--- 1. Más búsqueda ---")
    mas_busqueda()
    print("\n--- 2. split y join ---")
    mas_split_y_join()
    print("\n--- 3. Limpiar y alinear ---")
    limpiar_y_alinear()
    print("\n--- 4. Comprobaciones ---")
    mas_comprobaciones()
    print("\n--- 5. Recorrer ---")
    recorrer()

    print("\n--- 6. Frecuencias ---")
    print(frecuencias("banana"))                           # {'b': 1, 'a': 3, 'n': 2}
    print(caracter_mas_repetido("el perro de la casa"))    # 'e'
    print(palabras_repetidas("El gato y el perro y el pez"))   # ['el', 'y']

    print("\n--- 7. Eliminar y filtrar ---")
    print(quitar_vocales("Programación"))                  # Prgrmcn
    print(quitar_repetidos("banana"))                      # ban
    print(solo_letras("a1b2c3"), solo_digitos("a1b2c3"))   # abc 123
    print(quitar_signos("¡Hola, mundo!"))                  # Hola mundo
    print(sustituir_varios("hackeame", {"a": "4", "e": "3"}))   # h4ck34m3
    print(sustituir_con_translate("hola"))                 # h4l1

    print("\n--- 8. Comparar ---")
    print(son_anagramas("Roma", "amor"))                   # True
    comparar()

    print("\n--- 9. Validaciones ---")
    print(dni_valido("12345678Z"), dni_valido("12345678A"))     # True False
    print(matricula_valida("1782MBT"), matricula_valida("17MBT"))  # True False
    print(es_entero_texto("-5"), es_entero_texto("5.5"))        # True False

    print("\n--- 10. Ejercicios típicos ---")
    print(mayuscula_tras_punto("hola. que tal. bien"))     # Hola. Que tal. Bien
    print(comprimir("aaabccdddd"))                         # a3b1c2d4
    print(acronimo("Escuela Politécnica Superior"))        # EPS
    print(alternar_mayusculas("hola mundo"))               # HoLa mUnDo
    print(decimal_a_binario_texto(10))                     # 1010
    print(hora_a_texto(9, 5, 3), texto_a_hora("09:05:03")) # 09:05:03 (9, 5, 3)

    print("\n--- 11. Caracteres especiales ---")
    especiales()