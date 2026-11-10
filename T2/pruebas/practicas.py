# Archivo: practicas.py
# Asignatura: Informática - Programación básica (Temas 0, 1 y 2)
# Enfoque: Retos del tipo «Haz un programa que...»
#
# Contenidos:
# - Variables, tipos básicos, conversiones y operadores.
# - Expresiones aritméticas, relacionales y lógicas.
# - Entrada por teclado y salida formateada.
# - Condicionales if/elif/else y match/case.
# - Bucles for, while, range, break y continue.
# - Cadenas: recorrido, métodos básicos, búsqueda y formato.
# - Funciones y descomposición de problemas.
# - Módulos math y random.

MOSTRAR_SOLUCIONES = False


# =====================================================================
# BLOQUE A. VARIABLES, TIPOS Y OPERADORES
# =====================================================================

# ---------------------------------------------------------------------
# A.1 Variables y tipos básicos
# Declara las variables edad = 20, altura = 1.75 y nombre = 'Ana'.
# Muestra en una sola línea: 'Ana tiene 20 años y mide 1.75 metros'.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# A.2 Operaciones aritméticas
# Pide dos números enteros y muestra su suma, resta, producto, división,
# división entera y resto. Comprueba que el segundo número no sea cero
# antes de dividir.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# A.3 Conversión de tipos
# Parte de la cadena texto = '100'. Conviértela a entero, súmale 25 y
# muestra el resultado como texto. Después, pide al usuario su edad y
# muestra cuántos años tendrá dentro de 10 años.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# A.4 Porcentajes y formato decimal
# Pide el precio de un producto y el porcentaje de descuento. Calcula
# el precio final y muéstralo con exactamente dos decimales.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# A.5 Conversión de segundos
# Pide una cantidad de segundos y conviértela en horas, minutos y
# segundos. Por ejemplo, 3671 segundos son 1 hora, 1 minuto y 11 segundos.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# A.6 Funciones matemáticas
# Pide el radio de un círculo y calcula su longitud y su área. Muestra
# ambos resultados con dos decimales. Usa math.pi.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# A.7 Números aleatorios
# Genera un número entero aleatorio entre 1 y 100. Después, elige al azar
# un color de la lista ['rojo', 'verde', 'azul'] y muestra ambos resultados.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# =====================================================================
# BLOQUE B. CONDICIONALES Y LÓGICA
# =====================================================================

# ---------------------------------------------------------------------
# B.1 Clasificar un número
# Pide un número y muestra si es positivo, negativo o igual a cero.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# B.2 Año bisiesto
# Pide un año e indica si es bisiesto. Un año es bisiesto si es divisible
# por 400, o si es divisible por 4 pero no por 100.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# B.3 Validar una nota
# Pide una nota entre 0 y 10. Si está fuera del intervalo, muestra un
# mensaje de error. En caso contrario, indica si está suspenso (<5),
# aprobado (5 a <7), notable (7 a <9) o sobresaliente (>=9).
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# B.4 Decidir si salir a la calle
# Define las variables llueve y tengo_paraguas. Se sale si no llueve o si
# llueve y se tiene paraguas. Muestra 'SALGO' o 'ME QUEDO'.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# B.5 Tipo de triángulo
# Pide las longitudes de tres lados. Comprueba primero que sean positivas
# y que puedan formar un triángulo. Si lo forman, indica si es equilátero,
# isósceles o escaleno.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# B.6 Validar una edad
# Solicita una edad y repite la petición mientras no sea un entero entre
# 0 y 120, ambos incluidos. Cuando sea válida, muestra la edad aceptada.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# B.7 Menú con match/case
# Pide un número del 1 al 4 y muestra una operación: 1 sumar, 2 restar,
# 3 multiplicar y 4 dividir. Para cualquier otro valor, 'Opción no válida'.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# =====================================================================
# BLOQUE C. BUCLES FOR, WHILE Y RANGE
# =====================================================================

# ---------------------------------------------------------------------
# C.1 Recorrer una secuencia
# Recorre la lista ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
# e imprime cada día en una línea diferente.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# C.2 Recorrer con índices
# Dada la lista [10, 20, 30], muestra para cada elemento su posición y su
# valor con el formato 'Posición X tiene valor Y'.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# C.3 Múltiplos con range
# Muestra los números pares entre 0 y 20, ambos incluidos, usando el
# tercer argumento de range para avanzar de dos en dos.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# C.4 Suma mediante un acumulador
# Calcula la suma de todos los números enteros del 1 al 100 y muestra
# el resultado al terminar el bucle.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# C.5 Tabla de multiplicar
# Pide un número entero y muestra su tabla de multiplicar del 1 al 10.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# C.6 Validar una entrada con while
# Pide un número entero entre 1 y 10. Mientras el valor esté fuera de ese
# intervalo, vuelve a pedirlo. Cuando sea válido, muestra el número.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# C.7 Búsqueda con break
# Recorre los números del 1 al 10. Cuando encuentres el 7, muestra un
# mensaje y termina inmediatamente el bucle mediante break.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# C.8 Saltar iteraciones con continue
# Recorre los números del 0 al 9 e imprime todos excepto el 3 y el 7.
# Utiliza continue para saltar esas iteraciones.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# C.9 Calcular un factorial
# Pide un entero no negativo y calcula su factorial. Recuerda que 0! = 1.
# Resuélvelo con un bucle, sin usar math.factorial.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# C.10 Números primos
# Pide un entero y determina si es primo. Un número primo es mayor que 1
# y solo tiene dos divisores: 1 y él mismo.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# =====================================================================
# BLOQUE D. CADENAS DE CARACTERES
# =====================================================================

# ---------------------------------------------------------------------
# D.1 Analizar una frase
# Define una frase. Muestra el número de palabras, el número de caracteres
# sin contar espacios y la palabra más larga. Usa funciones diferentes.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# D.2 Contar un carácter
# Escribe una función contar_caracter(texto, caracter) que devuelva cuántas
# veces aparece un carácter en una cadena, sin distinguir mayúsculas y
# minúsculas.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# D.3 Transformar y ordenar palabras
# A partir de la frase 'Python es un lenguaje de programación', muestra
# la frase en mayúsculas, en minúsculas y las palabras ordenadas
# alfabéticamente.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# D.4 Comprobar si una palabra es capicúa
# Crea una función es_capicua(palabra) que devuelva True si la palabra se
# lee igual de izquierda a derecha que de derecha a izquierda. No distingas
# mayúsculas y minúsculas.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# D.5 Formatear una hora
# Escribe una función que reciba horas, minutos y segundos y devuelva una
# cadena con el formato HH:MM:SS, rellenando con ceros a la izquierda.
# Por ejemplo, (9, 5, 3) debe producir '09:05:03'.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# D.6 Crear un resumen de texto
# Define contar_palabras(texto), contar_caracter(texto, caracter) y
# resumen_texto(texto, caracter). La última función debe utilizar las dos
# anteriores y devolver un resumen con el número de palabras y las
# apariciones del carácter indicado.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# D.7 Comprobar una cadena
# Pide una cadena y comprueba si está formada únicamente por dígitos.
# Si lo está, conviértela a entero y muestra el doble. Si no, informa
# de que no es un número entero positivo escrito como texto.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# =====================================================================
# BLOQUE E. FUNCIONES Y RETOS INTEGRADORES DE EXAMEN
# =====================================================================

# ---------------------------------------------------------------------
# E.1 Analizar una lista de palabras
# Dada la lista ['Python', 'es', 'un', 'lenguaje', 'de', 'programación'],
# crea una función diferente para contar las palabras, sumar los caracteres,
# obtener la palabra más larga, convertir todas a mayúsculas y minúsculas,
# y devolverlas ordenadas alfabéticamente.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# E.2 Calculadora de áreas
# Crea una función para calcular el área de un cuadrado y otra para el área
# de un rectángulo. Pregunta qué figura se desea calcular y solicita solo
# las dimensiones necesarias. Rechaza dimensiones no positivas.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# E.3 Ordenar tres números
# Escribe una función ordenar_tres(a, b, c) que devuelva los tres números
# ordenados de menor a mayor. No utilices sorted ni sort.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# E.4 Velocidad media y multa de radar
# Un vehículo recorre 9.3 km. Pide el tiempo empleado en segundos y calcula
# la velocidad media en km/h. Si supera 100 km/h, calcula la multa:
# 100 € hasta 130; 300 € hasta 150; 400 € hasta 160; 500 € hasta 170;
# y 600 € por encima. Valida que el tiempo sea positivo.
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###


# ---------------------------------------------------------------------
# E.5 Calcular una aproximación de pi
# Aproxima pi mediante la serie de Gregory-Leibniz usando el número de
# términos indicado por el usuario: pi = 4(1 - 1/3 + 1/5 - 1/7 + ...).
# ---------------------------------------------------------------------
### CÓDIGO AQUÍ ###