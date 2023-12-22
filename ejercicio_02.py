# CONTEO PARES E IMPARES

par = 0
impar = 0

for cont in range(1, 11):
    print("NÚMERO", cont, ": ", end="")
    num = int(input())
    if (num % 2 == 0):
        par = par + 1
    else:
        impar = impar + 1

print("CANTIDAD DE PARES : ", par)
print("CANTIDAD DE IMPARES : ", impar)