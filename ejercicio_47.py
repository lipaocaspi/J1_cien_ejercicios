# CÁLCULO DE DÍAS TRANSCURRIDOS

print(f"Nro DE MES : ", end = "")
mes = int(input())
print(f"Nro DE DÍAS : ", end = "")
dia = int(input())

tiempo = (((mes - 1) * 30) + dia)

print(f"")
print(f"LOS DÍAS TRANSCURRIDOS SON : {tiempo}")