# MOSTRAR LAS LETRAS CONSONANTES

C = 0
S = 0
D = 0
L = 0
R = 0
M = 0
consonante = 0
refran = ""

print(f"Ingrese Refran : ", end = "")
ref = input()

for F in range(0, len(ref)):
    if (ref[F] != " "):
        refran = refran + ref[F]

for F in range(0, len(refran)):
    letra = refran[F].upper()
    if (letra == "C"):
        C = C + 1
    if (letra == "S"):
        S = S + 1
    if (letra == "D"):
        D = D + 1
    if (letra == "L"):
        L = L + 1
    if (letra == "R"):
        R = R + 1
    if (letra == "M"):
        M = M + 1
    if (letra != "A" and letra != "E" and letra != "I" and letra != "O" and letra != "U"):
        consonante = consonante + 1

print(f"CANTIDAD DE C : {C}")
print(f"CANTIDAD DE S : {S}")
print(f"CANTIDAD DE D : {D}")
print(f"CANTIDAD DE L : {L}")
print(f"CANTIDAD DE R : {R}")
print(f"CANTIDAD DE M : {M}")
print(f"CANTIDAD DE CONSONANTES : {consonante}")