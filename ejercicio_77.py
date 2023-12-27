# SUELDO DE UN TRABAJADOR

boni = 0
sueldoF = 0

print(f"09. CALCULAR EL SUELDO FINAL")
print(f"Ingrese Nombre : ", end = "")
nom = input()
print(f"Sueldo Básico : S/.", end = "")
sueldoB = float(input())
print(f"Nro de Hijos : ", end = "")
hijos = int(input())

if (hijos > 0):
    boni = sueldoB * 0.7

sueldoF = sueldoB + boni

print(f"")
print(f"BONIFICACIÓN : S/.{boni}")
print(f"SUELDO FINAL : S/.{sueldoF}")