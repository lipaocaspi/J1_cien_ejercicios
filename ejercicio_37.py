# TRIÁNGULO DE PASCAL

M = []

print(f"MOSTRAR EL TRIÁNGULO DE PASCAL")
print(f"INGRESE DIMENSIÓN [MENOS O IGUAL A 20] : ", end = "")
N = int(input())

for IZQ in range(N):
    M.append([])
    M[IZQ].append(1)
    for DER in range(1, IZQ):
        M[IZQ].append(M[IZQ - 1][DER - 1] + M[IZQ - 1][DER])
    if (N != 0):
        M[IZQ].append(1)

for IZQ in range(N):
    print(" " * (N - IZQ), end = "")
    for DER in range(0, IZQ + 1):
        print("{0:2}".format(M[IZQ][DER]), end = "")
    print()