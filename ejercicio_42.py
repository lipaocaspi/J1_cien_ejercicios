# CÁLCULO DE HORAS, MINUTOS Y SEGUNDOS

import math

print(f"CANTIDAD DE SEGUNDOS : ", end = "")
xseg = int(input())

hor = math.trunc(xseg / 3600)
min = math.trunc((xseg - (hor * 3600)) / 60)
seg = math.trunc(xseg - ((hor * 3600) + (min * 60)))

print(f"HORAS : {hor}")
print(f"MINUTOS : {min}")
print(f"SEGUNDOS : {seg}")