# MOSTRAR SI ESTÁ APROBADO O DESAPROBADO

print(f"INGRESE NOTA 01 : ", end = "")
n1 = int(input())
print(f"INGRESE NOTA 02 : ", end = "")
n2 = int(input())
print(f"INGRESE NOTA 03 : ", end = "")
n3 = int(input())

prom = (n1 + n2 + n3)/3

if (prom > 10.5):
    print(f"APROBADO CON {prom}")
else:
    print(f"DESAPROBADO CON {prom}")