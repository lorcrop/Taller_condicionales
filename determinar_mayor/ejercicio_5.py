# Inicio
print("........................")
n1 = float(input("Ingresa el primer número: "))
print("........................")

print(".........................")
n2 = float(input("Ingresa el segundo número: "))
print(".........................")

print("........................")
n3 = float(input("Ingresa el tercer número: "))
print("........................")

# Comparamos los números
if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3

# Mostramos el resultado
print("--------------------")
print("El número mayor es: "+str(mayor))
print("--------------------")