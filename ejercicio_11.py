# PRODUCTO DE N NÚMEROS

pro = 1
print("VALOR DE N : ", end = "")
N = int(input())
for f in range(1, N + 1):
    print(f, " ", end = "")
    pro = pro * f
print("")
print("PRODUCTO DE ", N, " ES : ", pro)