# CÁLCULO DE INTERÉS Y MONTO A PAGAR AL BANCO

monto = 1000
print("Nro. de meses : ", end = "")
meses = int(input())
intereses = (monto * (meses * 0.02))
totalp = monto + intereses
print("INTERESES : ", intereses)
print("TOTAL A PAGAR : ", totalp)