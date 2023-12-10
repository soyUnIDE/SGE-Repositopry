numero=1
numeros=[]
while numero!=0:
    numero=int(input("Introduce un número se detendrá cuando introduzcas 0: "))
    numeros.append(numero)
numero=int(input("Introduce un numero a buscar: "))
if numero in numeros:
    print(f"El número {numero} se encuentra en la posición {(numeros.index(numero))+1}.")
else:
    print(f"El número {numero} no se encuentra almacenado.")