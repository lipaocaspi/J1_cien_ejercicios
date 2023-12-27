# CÁLCULO GANANCIAS DE UNA GARITA DE CONTROL

tarifa = 0
bus = 0
van = 0
micro = 0
man = 0
noc = 0

print(f"GANANCIAS DE UNA GARITA DE CONTROL")
print(f"----------------------------------")
print(f"CANTIDAD DE VEHÍCULOS : ", end = "")
cantidad = int(input())
print(f"")

for cont in range(1, cantidad + 1):
    print(f">> TIPO DE VEHÍCULO Nro {cont}/{cantidad} : ")
    print(f"1. Ómnibus.")
    print(f"2. Minivan.")
    print(f"3. Micro.")
    print(f"OPCIÓN : ", end = "")
    tipo = int(input())
    if (tipo == 1):
        tarifa = 13
        bus = bus + tarifa
    elif (tipo == 2):
        tarifa = 10
        van = van + tarifa
    elif (tipo == 3):
        tarifa = 8
        micro = micro + tarifa
    print(f"TURNO (M/N) : ", end = "")
    turno = input()
    if (turno == "M"):
        man = man + tarifa
    else:
        noc = noc + tarifa
    print(f"")

print(f"")
print(f"IMPORTE DE TURNO MAÑANA : {man}")
print(f"IMPORTE DE TURNO NOCHE : {noc}")
print(f"")
print(f"IMPORTE DE ÓMNIBUS : {bus}")
print(f"IMPORTE DE MINIVAN : {van}")
print(f"IMPORTE DE MICRO : {micro}")