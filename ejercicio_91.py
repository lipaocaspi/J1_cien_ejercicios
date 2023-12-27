# COSTO DE UNA LLAMADA TELEFÓNICA

print(f"CLAVES DE DESTINO")
print(f"[1] Estados Unidos - $0.13")
print(f"[2] Canadá - $0.11")
print(f"[5] América del Sur - $0.52")
print(f"[6] América Central - $0.99")
print(f"[8] México - $0.17")
print(f"[9] Europa - $0.17")
print(f"[10] Asia - $0.20")
print(f"[15] África - $0.59")
print(f"[20] Oceanía - $0.28")

print(f"INGRESE CLAVE DESTINO : ", end = "")
clave = int(input())
print(f"DURACIÓN DE LA LLAMADA : ", end = "")
minutos = int(input())

if (clave == 1):
    print(f"COSTO : $.{minutos * 0.13}")
elif (clave == 2):
    print(f"COSTO : $.{minutos * 0.11}")
elif (clave == 5):
    print(f"COSTO : $.{minutos * 0.52}")
elif (clave == 6):
    print(f"COSTO : $.{minutos * 0.99}")
elif (clave == 8):
    print(f"COSTO : $.{minutos * 0.17}")
elif (clave == 9):
    print(f"COSTO : $.{minutos * 0.17}")
elif (clave == 10):
    print(f"COSTO : $.{minutos * 0.20}")
elif (clave == 15):
    print(f"COSTO : $.{minutos * 0.59}")
elif (clave == 20):
    print(f"COSTO : $.{minutos * 0.28}")
else:
    print(f"¡¡ Error en clave !!")