# NÚMEROS DE UN RANGO

print("NÚMERO A : ", end = "")
A = int(input())
print("NÚMERO B : ", end = "")
B = int(input())
if (A < B):
    for N in range(A + 1, B ):
        print(N)
else:
    for N in range(B + 1, A):
        print(N)