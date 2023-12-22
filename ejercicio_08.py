# 123456789
# 12345678
# 1234567
# 123456
# 12345
# 1234
# 123
# 12
# 1

for F in range(1, 10):
    serie = float(0)
    for C in range(1, 11 - F):
        S = float(10 - F)
        serie = (serie * 10) + C
    print(serie)