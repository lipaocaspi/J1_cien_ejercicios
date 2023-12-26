# COSTO TOTAL TENIENDO EN CUENTA EL TIEMPO

print("HORAS : ", end = "")
H = int(input())
print("MINUTOS : ", end = "")
M = int(input())
print("SEGUNDOS : ", end = "")
S = int(input())
costo = ((H * 3600) + (M * 60) + S) * 0.25
print("")
print("COSTO TOTAL : ", costo)