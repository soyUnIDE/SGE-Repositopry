lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
print(lista)
for i in range(len(lista[0])):
    if lista[0][i] >50:
        lista[0][i]=0
print(lista)