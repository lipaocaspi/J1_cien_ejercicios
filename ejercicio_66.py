# DIBUJO DE UN TRIÁNGULO SEGÚN EL CARACTER INGRESADO

print(f"Altura del Triángulo : ", end = "")
alt = int(input())
print(f"Ingrese un Caracter : ", end = "")
caract = input()

for i in range(1, alt + 1):
    for j in range(1, (alt - i) + 1):
        print(f" ", end = "")
    for j in range(1, (i * 2)):
        print(caract, end = "")
    print(f"")