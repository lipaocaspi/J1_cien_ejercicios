# 18% DEL MONTO INGRESADO

print(f"14. MOSTRAR 18% SI MONTO ES MAYOR A $500.")
print(f" ") 
print(f"INGRESE MONTO : $/.", end = "")
num = int(input())

if (num > 500):
    print(f"EL 18% ES : ${(num * 0.18)}")