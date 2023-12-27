# COSTO DE UNA LLAMADA TELEFÓNICA

print(f"CANTIDAD DE MINUTOS : ", end = "")
llamada = int(input())

if (llamada <= 5):
    costo = llamada * 0.9
else:
    costo = (5 * 0.9) + ((llamada - 5) * 1.1)

print(f"EL COSTO ES : S/.{costo}")