n=int(input("Introduce un valor entero positivo: "))
aux=n
invertido = 0
while n != 0:
    invertido = 10*invertido+n % 10
    n //= 10
print(f"El número {aux} al revés es: {invertido}")