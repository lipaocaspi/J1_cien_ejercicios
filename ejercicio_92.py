# CÁLCULO DEL COSTO MENSUAL POR EL TIPO DE SEGURO

print(f"TIPOS DE SEGURO")
print(f"1. X")
print(f"2. Y")
print(f"3. Z")
print(f"OPCIÓN : ", end = "")
seguro = int(input())

if (seguro == 1):
    print(f"Pago Mensual : $45")
elif (seguro == 2):
    print(f"Pago Mensual : $30")
elif (seguro == 3):
    print(f"Pago Mensual : $15")
else:
    print(f"Error en el tipo de seguro.")