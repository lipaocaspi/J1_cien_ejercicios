# ÁREA Y VOLUMEN DE UN CILINDRO

import math

print(f"RADIO : ", end = "")
r = float(input())
print(f"ALTURA : ", end = "")
h = float(input())

a = 2 * math.pi * r * (h + r)
v = math.pi * (r * r) * h

print(f"ÁREA TOTAL DEL CILINDRO : {a} cm2")
print(f"VOLUMEN DEL CILINDRO : {v} cm3")