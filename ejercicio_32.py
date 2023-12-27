# SE DAN REGALOS DEPENDIENDO DEL SEXO Y EDAD

diax = 27
mesx = 12
aniox = 2023
edad = 0

for x in range(1, 11):
    print(f"DNI : ", end = "")
    dni = input()
    print(f"DÍA DE NACIMIENTO : ", end = "")
    dia = int(input())
    print(f"MES DE NACIMIENTO : ", end = "")
    mes = int(input())
    print(f"AÑO DE NACIMIENTO : ", end = "")
    anio = int(input())
    print(f"GÉNERO (H/M) : ", end = "")
    genero = input()
    print(f"FECHA ACTUAL : {diax}/{mesx}/{aniox}")
    edad = aniox - anio
    if (mes > mesx):
        edad = edad - 1
    elif (mes == mesx and dia > diax):
        edad = edad - 1
    print(f"EDAD : {edad} años")
    if (edad >= 8):
        print(f"RECIBE TABLET")
    elif (edad == 6):
        if (genero == "H"):
            print(f"RECIBE CARRITO")
        else:
            print(f"RECIBE MUÑECA")

print(f"")