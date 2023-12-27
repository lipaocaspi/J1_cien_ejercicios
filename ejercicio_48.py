# MOSTRAR LA UNIDAD, CENTENA Y DECENA

print(f"INGRESE Nro DE 3 CIFRAS : ", end = "")
num = int(input())

cen = int((num - (num % 100)) / 100)
res = num % 100
dec = int((res - (res % 10)) / 10)
uni = res % 10

print(f"")
print(f"CENTENA : {cen}")
print(f"DECENA : {dec}")
print(f"UNIDAD : {uni}")