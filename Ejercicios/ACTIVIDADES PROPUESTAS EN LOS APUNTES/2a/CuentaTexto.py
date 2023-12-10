texto=input("Escribe un texto: ")
cont=0
for i in range(len(texto)):
    if (texto[i]=='P')and(texto[i+1]=='y')and(texto[i+2]=='t')and(texto[i+3]=='h')and(texto[i+4]=='o')and(texto[i+5]=='n'):
        cont=cont+1
print(f"En el texto hay escrito \"Python\" {cont} veces.")