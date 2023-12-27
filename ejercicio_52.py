# ÁREA Y PERÍMETRO DE UN TRAPECIO

print(f"ÁREA DEL TRAPECIO")
print(f"BASE MAYOR : ", end = "")
B = float(input())
print(f"BASE MENOR : ", end = "")
Bb = float(input())
print(f"ALTURA : ", end = "")
h = float(input())

A =  ((B * Bb) * h) / 2

print(f"ÁREA : {A} cm.")

print(f"")
print(f"PERÍMETRO DEL TRAPECIO")
print(f"LASO 01 : ", end = "")
l1 = float(input())
print(f"LASO 02 : ", end = "")
l2 = float(input())
print(f"LASO 03 : ", end = "")
l3 = float(input())
print(f"LASO 04 : ", end = "")
l4 = float(input())

P = l1 + l2 + l3 + l4

print(f"PERÍMETRO : {P} cm.")