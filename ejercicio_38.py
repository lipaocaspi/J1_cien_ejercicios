# COLOR MÁS VOTADO POR N CANTIDAD DE PERSONAS

r = 0
v = 0
a = 0

print(f"CANTIDAD DE PERSONAS : ", end = "")
N = int(input())

for i in range(1, N + 1):
    print(f"PERSONA Nro {i} ", end = "")
    c = ""
    while(c != "ROJO" and c != "VERDE" and c != "AZUL"):
        print(f"[ROJO - VERDE - AZUL] : ", end = "")
        c = input()
        c = c.upper()
    if (c == "ROJO"):
        r = r + 1
    elif (c == "VERDE"):
        v = v + 1
    else:
        a = a + 1

print(f"")

if (r > v and r > a):
    Mcolor = "ROJO"
elif(v > r and v > a):
    Mcolor = "VERDE"
else:
    Mcolor = "AZUL"
    
print(f"CANTIDAD DE COLOR ROJO : {r}")
print(f"CANTIDAD DE COLOR VERDE : {v}")
print(f"CANTIDAD DE COLOR AZUL : {a}")
print(f"EL COLOR ESCOGIDO ES : {Mcolor}")