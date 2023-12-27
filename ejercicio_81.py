# CÁLCULO IGV SI LA COMPRA ES MAYOR A $100

IGV = 0
monto = 0

print(f"05. CALCULAR IGV SEGÚN EL MONTO DE COMPRA")
print(f"INGRESE PRECIO : $/.", end = "")
precio = float(input())
print(f"INGRESE CANTIDAD : ", end = "")
cant = int(input())

monto = (precio * cant)

if (monto > 100):
    IGV = monto * 0.18

print(f"")
print(f"TOTAL   : S/.{monto}")
print(f"IGV 18%   : S/.{IGV}")
print(f"TOTAL A PAGAR   : S/.{(monto + IGV)}")