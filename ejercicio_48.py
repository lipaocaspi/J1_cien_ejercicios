# MOSTRAR LA UNIDAD, CENTENA Y DECENA

print("INGRESE Nro DE 3 CIFRAS : ", end = "")
num = int(input())
cen = int((num - (num % 100)) / 100)
res = num % 100
dec = int((res - (res % 10)) / 10)
uni = res % 10
print("")
print("CENTENA : ", cen)
print("DECENA : ", dec)
print("UNIDAD : ", uni)