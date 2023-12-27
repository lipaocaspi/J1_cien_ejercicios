# PROMEDIO DE VARIAS NOTAS

suma = 0

n = int(input(f"INGRESE LA CANTIDAD DE NOTAS : "))

for cont in range(1, n + 1):
    print(f"NOTA {cont} : ")
    nota = int(input())
    suma = suma + nota
    
print(f"PROMEDIO : {suma / n}")