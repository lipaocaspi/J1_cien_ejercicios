# CALCULAR EL DESCUENTO SEGÚN EL COLOR SORTEADO

import os
import random

desct = 0
compra = 0

print(f"VALOR DE COMPRA : S/.", end = "")
compra = float(input())
os.system("pause")
print(f"")

color = random.randint(1, 5)

if (color == 1):
    print(f"COLOR : BLANCO")
    desct = 1
elif (color == 2):
    print(f"COLOR : VERDE")
    desct = 0.5
elif (color == 3):
    print(f"COLOR : NEGRO")
    desct = 0.4
elif (color == 4):
    print(f"COLOR : CELESTE")
    desct = 0.05
elif (color == 5):
    print(f"COLOR : ROJO")
    desct = 0

print(f"DESCUENTO : S/.{desct}")
print(f"IMPORTE DESCT. : S/.{compra * desct}")
print(f"PAGO FINAL : S/.{compra - (compra * desct)}")