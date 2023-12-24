# PROMEDIO DE VARIAS NOTAS

suma = 0
n = int(input("INGRESE LA CANTIDAD DE NOTAS : "))

for cont in range(1, n + 1):
    print("NOTA ", cont, " : ")
    nota = int(input())
    suma = suma + nota
    
print("PROMEDIO : ", suma/n)