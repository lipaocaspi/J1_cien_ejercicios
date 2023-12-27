# LOGIN

print(f"INGRESE USUARIO : ", end = "")
usuario = input()
print(f"INGRESE CLAVE : ", end = "")
clave = int(input())

if (usuario == "ADMIN" and clave == 123456):
    print(f"ACCESO PERMITIDO")
else:
    print(f"ACCESO DENEGADO")