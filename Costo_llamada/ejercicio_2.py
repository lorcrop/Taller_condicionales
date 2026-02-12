# Inicio
T =int(input("Ingrese el tiempo de la llamda: "))

if T >= 3:
    P = (T * 3) * 100
    P = P + 500
elif T < 3:
    P = 500

print("..........................")
print("El valor de la llamada es:"+str(P))
print("..........................")
# Fin
