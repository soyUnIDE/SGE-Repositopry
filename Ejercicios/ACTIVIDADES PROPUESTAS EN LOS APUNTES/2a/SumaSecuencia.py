numero=input("Escribe una secuencia de numeros separada por espacios: ")
numeros= numero.split(" ")
suma=0
for i in numeros:
    suma+=int(i)
print(f"La suma de los valores es: {suma}")