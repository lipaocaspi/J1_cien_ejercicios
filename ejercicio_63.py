# CÁLCULO IVA

print(f"")
print(f"Costo de la Casa : $/.", end = "")
costo = float(input())
print(f"Valor del IVA : %.", end = "")
iva = float(input())
print(f"")

TotPagar = costo + (costo * (iva / 100))

print(f"IVA DE {iva}% : S/.{(costo * (iva / 100))}")
print(f"TOTAL A PAGAR : S/.{TotPagar}")