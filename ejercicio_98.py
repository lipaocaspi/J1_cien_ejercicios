# OBTENER ÁREA, BASE Y ALTURA DEL TRIÁNGULO

print(f" MENÚ DE OPCIONES DE UN TRIÁNGULO ")
print(f"----------------------------------")
print(f"1. Área de un triángulo, dada la base y la altura")
print(f"2. Base de un triángulo, dada la altura y el área")
print(f"3. Altura de un triángulo, dada la base y el área")
print(F"Selecciona una opción : ", end = "")
OPC = int(input())
print(f"")

if (OPC == 1):
    print(f"BASE : ", end = "")
    base = float(input())
    print(f"ALTURA : ", end = "")
    altura = float(input())
    area = (base * altura) / 2
    print(f"EL ÁREA ES : {area}")
elif (OPC == 2):
    print(f"ALTURA : ", end = "")
    altura = float(input())
    print(f"ÁREA : ", end = "")
    area = float(input())
    base = (area * 2) / altura
    print(f"LA BASE ES : {base}")
elif (OPC == 3):
    print(f"BASE : ", end = "")
    base = float(input())
    print(f"ÁREA : ", end = "")
    area = float(input())
    altura = (area * 2) / base
    print(f"LA ALTURA ES : {altura}")
else:
    print(f"Error... Opción Incorrecta")