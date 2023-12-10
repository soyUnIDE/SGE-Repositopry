lista=[]
for i in range(5):
    valor = int(input("Introduzca un valor: "))
    lista.append(valor)

print(f"Lista original: {lista}")
lista2=[]
posicion=0
while posicion<len(lista):
    if lista[posicion]>=10:
        lista2.append(lista.pop(posicion))
    else:
        posicion=posicion+1
print(f"La lista principal despues de borrar los elementos mayores o iguales a 10: {lista}")
print(f"La lista creada con los valores mayores o iguales a 10: {lista2}")