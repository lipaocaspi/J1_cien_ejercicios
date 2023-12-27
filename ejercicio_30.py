# CÁLCULO TOTAL DE VENTAS REALIZADAS

tv_h = 0
tv_m = 0
muj = 0

print(f"CANTIDAD DE EMPLEADOS : ", end = "")
empleados = int(input())

for cont in range(1, empleados + 1):
    print(f"EMPLEADO Nro {cont} / {empleados}")
    print(f"NOMBRE : ", end = "")
    num = input()
    print(f"GÉNERO (H/M) : ", end = "")
    genero = input()
    print(f"VENTAS : ", end = "")
    ventas = int(input())
    print(f"")
    if (genero == "H"):
        tv_h = tv_h + ventas
    else:
        tv_m = tv_m + ventas
        muj = muj + 1
        
print(f"TOTAL DE VENTAS HOMBRES : {tv_h}")
print(f"TOTAL DE VENTAS MUJERES : {tv_m}")
print(f"")
print(f"PORCENTAJE DE MUJERES : {(muj * 100)/empleados}%")