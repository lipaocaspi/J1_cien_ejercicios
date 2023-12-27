# MOSTRAR EL PORCENTAJE DE ALUMNOS APROBADOS Y DESAPROBADOS

print(f"MOSTRAR EL PORCENTAJE DE ALUMNOS APROBADOS Y DESAPROBADOS")
print(f"")
print(f"INGRESE LA CANTIDAD DE ALUMNOS APROBADOS : ", end = "")
apro = int(input())
print(f"INGRESE LA CANTIDAD DE ALUMNOS DESAPROBADOS : ", end = "")
desa = int(input())
print(f"")

porA = (apro * 100) / (apro + desa)
porB = (desa * 100) / (apro + desa)

print(f"APROBADOS : {round(porA * 100) / 100}%")
print(f"DESAPROBADOS : {round(porB * 100) / 100}%")