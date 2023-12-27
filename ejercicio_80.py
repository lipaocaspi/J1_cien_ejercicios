# CÁLCULO BONIFICACIÓN

print(f"04. CALCULAR BONIFICACIÓN")
print(f"")
print(f"INGRESE MONTO DE VENTA : $.", end = "")
venta = float(input())

if (venta > 2000):
    print(f"BONIFICACIÓN 10% : $.{venta * 0.10}")
else:
    print(f"BONIFICACIÓN 50% : $.{venta * 0.50}")