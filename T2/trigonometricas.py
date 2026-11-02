import math	                # Con prefijo math.
from math import cos	    # Sin prefijo solo esa función	cos(x)
from math import *	        # Sin prefijo, todas las funciones

print(math.sin(0))          # Seno con radianes
print(math.cos(math.pi))    # Coseno con radianes
print(math.tan(0))          # Tangente con radianes
print(math.exp(2.5))        # Nos da e^x
print(math.ceil(2.5))       # Redondeo arriba de x.
print(math.floor(2.5))      # Redondeo abajo de x.
print(math.log(2.5))        # Logaritmo neperiano de x
print(math.log10(2.5))      # Logaritmo decimal de x
print(math.sqrt(2.5))       # Raíz cuadrada de x
print(math.pow(2.5, 3))     # Potencia x^n
print(2.5**3)               # Potencia x^n
#Consola print(pow(2, 3, 4))  # Potencia x^n

print(math.pi)
print(math.e)

print("-"*50)
print(ceil(1.001))          # Redondea hacia arriba
print(floor(1.001))         # Redondea hacia abajo
print(factorial(10))
print(gcd(10,125))          # MCD(10,125)
print("-"*5)
print(trunc(1.001))         # Truncar
print(trunc(1.999))
print("-"*5)
print(round(1.001))         # Aproximar
print(round(1.499999999))
print(round(1.5))
print(round(1.999))
print("-"*5)
print(hypot(3,4))
print(asin(0.7071067811865476))
print(acos(0.7071067811865476))
print(atan(0.5773502691896257))