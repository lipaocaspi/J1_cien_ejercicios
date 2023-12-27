# MOSTRAR EL DÍA DE LA SEMANA

print(f"INGRESE DÍA [1-7]: ", end = "")
dia = int(input())

if (dia == 1):
    print(f"LUNES")
elif (dia == 2):
    print(f"MARTES")
elif (dia == 3):
    print(f"MIERCOLES")
elif (dia == 4):
    print(f"JUEVES")
elif (dia == 5):
    print(f"VIERNES")
elif (dia == 6):
    print(f"SÁBADO")
elif (dia == 7):
    print(f"DOMINGO")
else:
    print(f"Día Inválido")