# CÁLCULO DEL MONTO A PAGAR

total = 0
desc = 0

for cont in range(1, 11):
    print(f"CONSUMO {cont} : $. ", end="")
    consumo = float(input())
    total = total + consumo

if (total > 50):
    desc = total * 0.07

print(f"CONSUMO TOTAL : $.{total}")
print(f"DESCUENTO : $.{desc}")
print(f"PAGO TOTAL : $.{total - desc}")