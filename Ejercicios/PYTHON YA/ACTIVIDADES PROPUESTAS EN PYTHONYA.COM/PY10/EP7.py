negativos=0
positivos=0
mul15=0
sumPar=0
for i in range(10):
    numero=int(input(f"Introduce un numero: "))
    if numero>0:
        positivos+=1
    else:
        negativos+=1
    if numero%2==0:
        sumPar+=numero
    if numero%15==0:
        mul15+=1
print(f"En los numeros introducidos hay {negativos} negativos, {positivos} positivos, {mul15} múltimplos de 15 y la suma total de todos los numeros pares es {sumPar}.")