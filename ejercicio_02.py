# CONTEO PARES E IMPARES

par = 0
impar = 0

for cont in range(1, 11):
    print(f"NÚMERO {cont} : ", end="")
    num = int(input())
    if (num % 2 == 0):
        par = par + 1
    else:
        impar = impar + 1

print(f"CANTIDAD DE PARES : {par} ")
print(f"CANTIDAD DE IMPARES : {impar}")