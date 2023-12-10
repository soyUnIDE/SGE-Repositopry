total=int(input("Total de preguntas: "))
bien=int(input("Total de preguntas acertadas: "))
porcent= (bien/total)*100
if porcent>=90:
    print("Nivel máximo.")
elif porcent>=75 and porcent<90:
    print("Nivel medio.")
elif porcent>=50 and porcent<75:
    print("Nivel regular.")
elif porcent<50:
    print("Fuera de nivel.")