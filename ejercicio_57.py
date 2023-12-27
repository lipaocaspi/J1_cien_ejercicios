# MUESTRA LOS DÍAS, MESES Y AÑOS

import math

print(f"INGRESE CANTIDAD DE DÍAS : ", end = "")
dias = int(input())

A = math.trunc(dias / 365)
M = math.trunc((dias - (A * 365)) / 30)
D = math.trunc(dias - ((A * 365) + (M * 30)))

print(f"Año : {A}")
print(f"Mes : {M}")
print(f"Día : {D}")