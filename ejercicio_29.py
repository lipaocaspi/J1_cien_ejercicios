# MUESTRA LA CANTIDAD DE NÚMEROS PARES E IMPARES

sumaP = 0
sumaI = 0

print("INGRESE NÚMERO : ", end = "")
num = int(input())
for x in range(1, num + 1):
    if ((x % 2) == 0):
        sumaP = sumaP + x
    elif ((x % 2) == 1):
        sumaI = sumaI + x
print("Suma de pares : ", sumaP)
print("Suma de impares : ", sumaI)