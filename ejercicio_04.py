# ALUMNO CON MAYOR PROMEDIO

xpro = 0

for cont in range(1, 6):
    print(f"NOMBRE : ", end="")
    nom = input()
    print(f"PROMEDIO : ", end="")
    pro = float(input())
    if (xpro < pro):
        xpro = pro
        xnom = nom
    
print(f"ALUMNO CON MAYOR NOTA : {xnom}")
print(f"PROMEDIO : {xpro}")