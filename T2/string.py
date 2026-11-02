from math import pi,e
t = "Hola Mundo"
t1 = "hola"
t2 = "hola mundo"

print(str.lower(t))
print(t.lower())
print(str.upper(t))
print(str.islower(t))
print(str.isupper(t))
s = "   hola   "
print(str.strip(s))
print(str.isdigit("123"))
print(str.isalpha("hola"))
print(str.isspace("   "))
print(t2.title())
print(str.find(t2, t1))

print("{1}, {0} y {2}".format(1, 2, 3))

print("-"*50)
nombre = "Juan"
edad = 30
print("Hola, mi nombre es {} y tengo {} años.".format(nombre, edad))
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

print("-"*50)
print(f"pi:{pi:5.2f}.")                  # quiero que el resultado ocupe como mínimo 5 caracteres, y que tenga 2 decimales
print(f"pi:{pi:0.2f}.")                  # quiero que el resultado ocupe como mínimo 0 caracteres, y que tenga 2 decimales
print("{0:5.2f}" .format(pi))
print("{0:5.2f} y {1:5.2f}".format(pi, e))
print(str.format("{0:5.30f}",pi))
print(str.format("{0:08.4f}", pi))
print(str.format("{0:15s}", "Hola, mundo que tal estais?"))
print("{0:15.15s}".format("Hola, mundo que tal estais?"))

print("-"*50)
print(str.format("{0:4d}", 128))
print(str.format("{0:4x}", 128))
print(str.format("{0:4o}", 128))
print(str.format("{0:4b}", 128))

print("-"*50)
una_cadena='abc'.replace('b','B')
print(una_cadena)