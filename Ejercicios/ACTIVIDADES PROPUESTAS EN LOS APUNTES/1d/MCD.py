n1=int(input("Introduce el primer número: "))
n2=int(input("Introduce el segundo número: "))
tem1=n1
tem2=n2
temporal=0
while n2!=0:
    print(f"Dividimos {n1} y {n2} el restultado es {n1%n2}")
    temporal=n2
    n2=n1%temporal
    n1=temporal
print(f"El MCD de {tem1} y {tem2} es {n1}")