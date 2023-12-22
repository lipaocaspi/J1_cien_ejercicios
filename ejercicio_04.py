# ALUMNO CON MAYOR PROMEDIO

xpro = 0

for cont in range(1, 6):
    print("NOMBRE : ", end="")
    nom = input()
    print("PROMEDIO : ", end="")
    pro = float(input())
    if (xpro < pro):
        xpro = pro
        xnom = nom
    
print("ALUMNO CON MAYOR NOTA : ", xnom)
print("PROMEDIO : ", xpro)