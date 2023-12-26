# ÁREA Y PERÍMETRO DE UN TRAPECIO

print("ÁREA DEL TRAPECIO")
print("BASE MAYOR : ", end = "")
B = float(input())
print("BASE MENOR : ", end = "")
Bb = float(input())
print("ALTURA : ", end = "")
h = float(input())
A =  ((B * Bb) * h) / 2
print("ÁREA : ", A, "cm.")
print("")
print("PERÍMETRO DEL TRAPECIO")
print("LASO 01 : ", end = "")
l1 = float(input())
print("LASO 02 : ", end = "")
l2 = float(input())
print("LASO 03 : ", end = "")
l3 = float(input())
print("LASO 04 : ", end = "")
l4 = float(input())
P = l1 + l2 + l3 + l4
print("PERIMETRO : ", P, "cm.")