import math
import random

random.seed()
#random.seed(42)

c1= random.randint(1,100)
c2= random.randint(1,100)
h= math.sqrt((c1**2) + (c2**2))
print("La hipotenusa del triángulo de catetos ",c1," y ",c2," es ",h)

print(random.choice(('rojo','verde','azul')))