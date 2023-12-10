n1=int(input("Dime cuantos numeros vas a introducir: "))
print(f"Escribe {n1} números:")
mayor=-100000
menor=100000
for i in range(n1):
    n2=int(input(f"Número {i+1}: "))
    if mayor<n2:
        mayor=n2
    if menor>n2:
        menor=n2
print(f"El número mayor es {mayor}\nEl número menor es {menor}")