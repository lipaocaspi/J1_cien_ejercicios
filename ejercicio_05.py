# 10 NÚMEROS DE FIBONACCI

A = 0
B = 1
C = 0

for cont in range(1, 11):
    print(f"{C} ")
    A = B
    B = C
    C = A + B