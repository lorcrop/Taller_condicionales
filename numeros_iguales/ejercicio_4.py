# inicio
n= input("Ingrese un número: ")

# Verificar que tenga al menos dos dígitos
if len(n) < 3:
    print("El número debe tener al menos tres dígitos.")
else:
    # Obtener los dos últimos dígitos
    ultimo = n[-1]
    penultimo = n [-2]

    # Comparar
    if ultimo == penultimo:
        print("Los dos últimos dígitos son iguales ")
    else:
        print("Los dos últimos dígitos son diferentes ")
