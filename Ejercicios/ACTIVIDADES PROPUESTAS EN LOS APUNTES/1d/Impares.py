n1=int(input("Introduce un número entero positivo: "))
linea=""
for i in range(1,n1,2):
    linea+=f"{i}, "
print(linea)