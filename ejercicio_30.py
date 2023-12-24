# CÁLCULO TOTAL DE VENTAS REALIZADAS

tv_h = 0
tv_m = 0
muj = 0

print("CANTIDAD DE EMPLEADOS : ", end = "")
empleados = int(input())
for cont in range(1, empleados + 1):
    print("EMPLEADO Nro ", cont, "/", empleados)
    print("NOMBRE : ", end = "")
    num = input()
    print("GÉNERO (H/M) : ", end = "")
    genero = input()
    print("VENTAS : ", end = "")
    ventas = int(input())
    print("")
    if (genero == "H"):
        tv_h = tv_h + ventas
    else:
        tv_m = tv_m + ventas
        muj = muj + 1
print("TOTAL DE VENTAS HOMBRES : ", tv_h)
print("TOTAL DE VENTAS MUJERES : ", tv_m)
print("")
print("PORCENTAJE DE MUJERES : ", (muj * 100)/empleados, "%")