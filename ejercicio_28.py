# MOSTRAR SI UN NÚMERO ES PRIMO

divisi = 0
print("INGRESE NÚMERO : ", end = "")
num = int(input())

for divi in range(1, num + 1):
    if ((num % divi) == 0):
        divisi = divisi + 1
if (divisi == 2):
    print("NÚMERO PRIMO")
else:
    print("NO ES PRIMO")