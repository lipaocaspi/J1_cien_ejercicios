# CALCULAR EL MONTO TOTAL A PAGAR EN UNA COMPRA DE TECLADOS

print(f"INGRESE CANTIDAD A COMPRAR : ", end = "")
cantidad = int(input())

if (cantidad >= 1 and cantidad <= 3):
    costo = float(15)
elif (cantidad >= 4 and cantidad <= 8):
    costo = float(11)
else:
    costo = float(10)

print(f"Costo por teclado : S/.{costo}")
print(f"Total a Pagar : S/.{costo * cantidad}")