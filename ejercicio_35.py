# TRIÁNGULO EQUILÁTERO DE NÚMEROS EN SECUENCIA

num = 0
val = 1
contador = 1

print(f"MUESTRA GRÁFICA DE NÚMEROS COMO TRIÁNGULO.")

while (num < 3):
    print(f"INGRESE NÚMERO : ", end = "")
    num = int(input())
print("")

for x in range(1, num + 1):
    espa = ""
    for z in range(1, num - x + 1):
        espa = espa + " "
    print(espa, end = "")
    contador = 1
    for f in range(1, val + 1):
        print(contador, end = "")
        if (contador == 9):
            contador = 0
        else:
            contador = contador + 1
    val = val + 2
    print(f"")