mañana=[]
tarde=[]
noche=[]
for i in range(5):
    edad=int(input("Introduce la edad de un estudiante de por la mañana: "))
    mañana.append(edad)
for i in range(6):
    edad=int(input("Introduce la edad de un estudiante de por la tarde: "))
    tarde.append(edad)
for i in range(11):
    edad=int(input("Introduce la edad de un estudiante de por la noche: "))
    noche.append(edad)

prodMañana=0
sumMañana=0

prodTarde=0
sumTarde=0

prodNoche=0
sumNoche=0

for i in range(len(mañana)):
    sumMañana+=mañana[i]
for i in range(len(tarde)):
    sumTarde+=tarde[i]
for i in range(len(noche)):
    sumNoche+=noche[i]

prodMañana=sumMañana/len(mañana)
prodTarde=sumTarde/len(tarde)
prodNoche=sumNoche/len(noche)
if prodMañana>prodTarde and prodMañana>prodNoche:
    print(f"El horario con un promedio mayor es el de la mañana con un promedio de {prodMañana} años")
elif prodTarde>prodMañana and prodTarde>prodNoche:
    print(f"El horario con un promedio mayor es el de la tarde con un promedio de {prodTarde} años")
elif prodNoche>prodTarde and prodNoche>prodMañana:
    print(f"El horario con un promedio mayor es el de la noche con un promedio de {prodNoche} años")