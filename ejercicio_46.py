# COSTO TOTAL TENIENDO EN CUENTA EL TIEMPO

print(f"HORAS : ", end = "")
H = int(input())
print(f"MINUTOS : ", end = "")
M = int(input())
print(f"SEGUNDOS : ", end = "")
S = int(input())

costo = ((H * 3600) + (M * 60) + S) * 0.25

print(f"")
print(f"COSTO TOTAL : {costo}")