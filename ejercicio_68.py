# CALCULAR EL SALARIO DE UN TRABAJADOR

SueldoBase = 0
num_hijos = 0
dias_no_laborables = 0
sueldo_final = 0

print(f"CALCULAR EL SUELDO FINAL DE UN EMPLEADO")
print(f"")
print(f"Ingrese Sueldo Base : $", end = "")
SueldoBase = float(input())
print(f"Ingrese Número de Hijos : ", end = "")
num_hijos = int(input())
print(f"Ingrese Días no Laborables Trabajados : ", end = "")
dias_no_laborables = int(input())

sueldo_final = SueldoBase + (num_hijos * 100) +(dias_no_laborables * 25)

print(f"")
print(f"SUELDO FINAL : ${sueldo_final}")