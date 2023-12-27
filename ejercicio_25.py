# SERIE 1 + 2/3 + 3/5 + 4/7...

print(f"VALOR DE N : ", end = "")
n = int(input())

suma = 1
d = 3

if (n > 1):
    print(f"{suma} + ", end = "")
    for i in range(2, n + 1):
        if (i == n):
            print(f"{i} / {d}", end = "")
        else:
            print(f"{i} / {d} + ", end = "")
        suma = suma + (i/d)
        d = d + 2
        
print(f"")
print(f"La suma es : {suma}")