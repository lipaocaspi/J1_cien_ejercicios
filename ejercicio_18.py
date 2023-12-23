# NÚMERO CAPICÚA

tem = ""
print("INGRESE NÚMERO : ", end = "")
num = input()
for i in reversed(range(0, len(num))):
    tem = tem + num[i]
print("")
print("NÚMERO INGRESADO : ", num)
print("NÚMERO CAMBIADO : ", tem)
if (num == tem):
    print("SI ES UN NÚMERO CAPICÚA")
else:
    print("NO ES UN NÚMERO CAPICÚA")