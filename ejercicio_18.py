# NÚMERO CAPICÚA

tem = ""

print(f"INGRESE NÚMERO : ", end = "")
num = input()

for i in reversed(range(0, len(num))):
    tem = tem + num[i]

print(f"")
print(f"NÚMERO INGRESADO : {num}")
print(f"NÚMERO CAMBIADO : {tem}")

if (num == tem):
    print(f"SI ES UN NÚMERO CAPICÚA")
else:
    print(f"NO ES UN NÚMERO CAPICÚA")