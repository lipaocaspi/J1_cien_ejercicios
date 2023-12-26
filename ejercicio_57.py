# MUESTRA LOS DÍAS, MESES Y AÑOS

import math

print("INGRESE CANTIDAD DE DÍAS : ", end = "")
dias = int(input())
A = math.trunc(dias / 365)
M = math.trunc((dias - (A * 365)) / 30)
D = math.trunc(dias - ((A * 365) + (M * 30)))
print("Año : ", A)
print("Mes : ", M)
print("Día : ", D)