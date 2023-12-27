# PRODUCTO DE N NÚMEROS

pro = 1

print(f"VALOR DE N : ", end = "")
N = int(input())

for f in range(1, N + 1):
    print(f"{f} ", end = "")
    pro = pro * f
    
print(f"")
print(f"PRODUCTO DE {N} ES : {pro}")