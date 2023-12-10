lista=[]
for i in range(5):
    valor = int(input("Introduzca un valor: "))
    lista.append(valor)

mayor=lista[0]
menor=lista[0]
for i in range(1,len(lista)):
    if lista[i]>mayor:
        mayor=lista[i]
    elif lista[i]<menor:
        menor=lista[i]

print(f"El mayor elemento de la lista es: {mayor}")
print(f"El menor elemento de la lista es: {menor}")