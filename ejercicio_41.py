# PAGO SALARIO CON 20% DE DESCUENTO

print(f"INGRESE SALARIO : ", end = "")
salario = float(input())

desc = (salario * 0.2)

print(f"Descuento del 20% : {desc}")
print(f"Nuevo salario : {(salario - desc)}")