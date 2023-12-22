# CÁLCULO DEL MONTO A PAGAR

total = 0
desc = 0

for cont in range(1, 11):
    print("CONSUMO", cont, ": $. ", end="")
    consumo = float(input())
    total = total + consumo

if (total > 50):
    desc = total * 0.07

print("CONSUMO TOTAL : $.", total)
print("DESCUENTO : $.", desc)
print("PAGO TOTAL : $.", total - desc)