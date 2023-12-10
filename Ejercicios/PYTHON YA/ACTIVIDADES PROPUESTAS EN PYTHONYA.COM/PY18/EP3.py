lista=[2,5,8,7,1]
print(lista)
for k in range(4):
    for x in range(4-k):
        if lista[x]>lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux
print(lista)
for k in range(4):
    for x in range(4-k):
        if lista[x]<lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux
print(lista)