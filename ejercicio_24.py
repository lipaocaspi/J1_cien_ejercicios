# FACTORIAL DE UN NÚMERO

fact = 1
print("FACTORIAL A CALCULAR : ", end = "")
num = int(input())
print("")
print("SERIE DEL FACTORIAL : ", end = "")
for x in range(1, num + 1):
    print((num + 1) - x, "", end = "")
    fact = fact * x
print("")
print("EL FACTORIAL ES : ", fact)
print("")