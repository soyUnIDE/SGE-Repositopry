texto=input("Escribe una oración: ")
texto.upper()
cont=0
for i in range(len(texto)):
    if (texto[i]=='a')or(texto[i]=='e')or(texto[i]=='i')or(texto[i]=='o')or(texto[i]=='u'):
        cont=cont+1
print(f"En la oración hay {cont} vocales.")