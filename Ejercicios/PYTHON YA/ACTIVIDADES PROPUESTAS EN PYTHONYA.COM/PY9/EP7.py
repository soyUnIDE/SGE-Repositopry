numeros=int(input("Cuantos numeros quieres ingresar: "))
x=0
par=0
impar=0
while x<numeros:
    numero=int(input("Introduce un número: "))
    x+=1
    if numero%2==0:
        par+=1
    else:
        impar+=1
print(f"En {numeros} numeros hay {par} numeros pares y {impar} numeros impares.")