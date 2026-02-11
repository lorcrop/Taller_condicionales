# Inicio
print("..........")
print("Bienvenido")
print("..........")

print("-------------------------------")
P= int(input("Ingrese el valor de el producto "))
print("-------------------------------")

# Proceso 

if P <= 3000:
    Ganancia=P*0.15
else:
    if P > 6000:
        Ganancia= P*0.25
    else:
        Ganancia= 500

# Precio Final 

P_c=P+Ganancia

# Salida
print(".....................")
print("La ganancia es: "+str(Ganancia))
print(".....................")

print(".........................")
print("El Precio Final es "+str(P_c))
print(".........................")
