# MOSTRAR LA CANTIDAD DE VOCALES QUE HAY EN UNA FRASE

a = 0
e = 0
i = 0
oo = 0
u = 0
vocal = ""

print(f"FRASE : ", end = "")
frase = input()

for cont in range(0, len(frase)):
    vocal = frase[cont].upper()
    if (vocal == "A" or vocal == "Á"):
        a = a + 1
    if (vocal == "E" or vocal == "É"):
        e = e + 1
    if (vocal == "I" or vocal == "Í"):
        i = i + 1
    if (vocal == "O" or vocal == "Ó"):
        oo = oo + 1
    if (vocal == "U" or vocal == "Ú"):
        u = u + 1

print(f"CANTIDAD DE VOCALES : ")
print(f"A : {a}")
print(f"E : {e}")
print(f"I : {i}")
print(f"O : {oo}")
print(f"U : {u}")