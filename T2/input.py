base = float(input("Dame la base:"))
altura = float(input("Dame la altura:"))
area = (base*altura)/2

print("Base =", base,end=" ")
print("Altura =", altura,end=" ; ")
print("Area =", area)

print("-"*5)
print("Base =", base,end=" \n")
print("Altura =", altura,end=" ;\t; ")
print("Area =", area)

print("-"*5)
print(f"Base ={base}\n")
print(f"Altura = {altura}",end=" ")
print(f"Area = {area}")

unNombre=input("Dame tu nombre:")
edad=input("Dime tu edad:")
unNombre_str = str(unNombre)
edad_int = int(edad)
print(unNombre, "tiene", edad, "años de edad.")
print(f"{unNombre} tiene {edad} años de edad.")
#print("%s tiene %d años de edad." % (unNombre, edad))
print("%s tiene %d años de edad." % (unNombre_str, edad_int))