# CÁLCULO DE HORAS, MINUTOS Y SEGUNDOS

import math

print("CANTIDAD DE SEGUNDOS : ", end = "")
xseg = int(input())
hor = math.trunc(xseg / 3600)
min = math.trunc((xseg - (hor * 3600)) / 60)
seg = math.trunc(xseg - ((hor * 3600) + (min * 60)))
print("HORAS : ", hor)
print("MINUTOS : ", min)
print("SEGUNDOS : ", seg)