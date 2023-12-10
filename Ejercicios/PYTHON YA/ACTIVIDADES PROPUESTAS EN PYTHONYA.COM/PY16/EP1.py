nombres=[]
for i in range(5):
    nombre = input("Introduce un nombre: ")
    nombres.append(nombre)
nombres.sort()
print(f"El nombre de la última persona ordenada por orden alfabético es {nombres[-1]}")