# ENCONTRAR UN NÚMERO ALEATORIO ENTRE 1 Y 20

import random

sw = 0
numA = random.randint(1, 21)

for i in range(1, 4):
    num = int(input(f"ENCUENTRE EL NÚMERO [1-20] : "))
    if (num == numA):
        print(f"NÚMERO ENCONTRADO")
        sw = 1
        i = 4
    else:
        if (num > numA):
            print(f"INGRESE UN NÚMERO MENOR")
        else:
            print(f"INGRESE UN NÚMERO MAYOR")
    print(f"")
    
if (sw == 0):
    print(f"EL NÚMERO A ENCONTRAR ERA : {numA}")