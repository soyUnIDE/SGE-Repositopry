oracion = input("Introduce una oración: ")
cont=0
for i in range(len(oracion)):
    if (oracion[i]==' '):
        cont=cont+1
print(f"En la oración hay escrito {cont} espacios.")