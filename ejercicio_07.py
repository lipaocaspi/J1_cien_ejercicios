# 999999999
# 88888888
# 7777777
# 666666
# 55555
# 4444
# 333
# 22
# 1

for F in range(1, 10):
    s = float(0)
    serie = float(0)
    for C in range(1, 11 - F):
        S = float(10 - F)
        serie = (serie * 10) + S
    print(serie)