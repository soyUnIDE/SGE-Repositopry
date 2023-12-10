n=int(input("Introduce tamaño de la tabla: "))
numeros=[]
bol=False
for i in range(n):
    lista=[]
    for j in range(n):
        lista.append(int(input("Introduce un número: ")))
    numeros.append(lista)

for i in range(len(numeros)):
    if (1 in numeros[i]) and (0 in numeros[i]):
        if numeros[i].index(1)==i and numeros[i].index(0)!=i:
            bol=True
        else:
            bol=False
    else:
        bol=False
if bol:
    print("La matriz es una matriz de identidad.")
else:
    print("La matriz no es una matriz de identidad.")