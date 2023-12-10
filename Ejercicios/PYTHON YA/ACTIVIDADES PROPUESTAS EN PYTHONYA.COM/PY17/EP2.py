nombres=[]
notas=[]
cont=0
for i in range(4):
    nombre = input("Introduce el nombre del alumno: ")
    nombres.append(nombre)
    nota=int(input(f"Introduce la nota de {nombre}: "))
    notas.append(nota)
for i in range(4):
    if notas[i]>=8:
        print(f"{nombres[i]}: Muy bueno")
        cont+=1
    else:
        if  notas[i]>=4:
           print(f"{nombres[i]}: Bueno")
        else:
            print(f"{nombres[i]}: Insuficiente")
print(f"La cantidad de alumnos muy buenos es de {cont}.")