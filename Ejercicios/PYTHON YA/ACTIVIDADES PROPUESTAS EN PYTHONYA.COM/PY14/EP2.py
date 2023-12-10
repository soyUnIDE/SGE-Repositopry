n=5
numeros=[8,2,6,4,9]
pantalla=[]
for i in range(len(numeros)):
    if numeros[i]>7:
        pantalla.append(numeros[i])
print(f"Los numeros mayores de 7 en la lista son {pantalla}")