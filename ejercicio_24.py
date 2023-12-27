# FACTORIAL DE UN NÚMERO

fact = 1

print(f"FACTORIAL A CALCULAR : ", end = "")
num = int(input())

print(f"")
print(f"SERIE DEL FACTORIAL : ", end = "")

for x in range(1, num + 1):
    print(f"{(num + 1) - x} ", end = "")
    fact = fact * x
    
print(f"")
print(f"EL FACTORIAL ES : {fact}")
print(f"")