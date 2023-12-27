# CUATRO OPERACIONES BÁSICAS

print(f"NÚMERO 1 : ", end = "")
num1 = int(input())
print(f"NÚMERO 2 : ", end = "")
num2 = int(input())
print(F"OPERADOR : ")
print(f"[1 +][2 -][3 x][4 /] : ", end = "")
operador = int(input())

if (operador == 1):
    print(f"SUMA : {(num1 + num2)}")
elif (operador == 2):
    print(f"RESTA : {(num1 - num2)}")
elif (operador == 3):
    print(f"MULTIPLICACIÓN : {(num1 * num2)}")
elif (operador == 4):
    print(f"DIVISIÓN : {(num1 / num2)}")
else:
    print(f"OPERADOR INCORRECTO")