# TOTAL A PAGAR POR LA COMPRA DE TECLADOS

cantidad = int(input(f"Cantidad a comprar : "))

if (cantidad >= 1 and cantidad <= 3):
    costo = 15
elif (cantidad >= 4 and cantidad <= 8):
    costo = 11
else:
    costo = 10

print(f"Costo por teclado : S/.{costo}")
print(f"Total a Pagar : S/.{costo * cantidad}")