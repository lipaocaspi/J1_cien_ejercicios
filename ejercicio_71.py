# MOSTRAR SI UN NÚMERO ES PAR O IMPAR

print(f"INGRESE NÚMERO : ", end = "")
num = int(input())

c = round(num / 2)
r = c * 2
re = num - r

if (re == 0):
    print(f"NÚMERO PAR")
else:
    print(f"NÚMERO IMPAR")