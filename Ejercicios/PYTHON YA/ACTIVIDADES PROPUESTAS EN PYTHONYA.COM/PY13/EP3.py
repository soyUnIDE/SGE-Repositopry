texto=input("Escribe una clave: ")
if (len(texto)<21)and(len(texto)>9):
    print("Clave valida.")
else:
    print("Clave no valida.")