sMañana=[]
sTarde=[]
for i in range(4):
    sueldo=int(input("Ingrese un sueldo del turno de mañana: "))
    sMañana.append(sueldo)
for i in range(4):
    sueldo=int(input("Ingrese un sueldo del turno de tarde: "))
    sTarde.append(sueldo)
print(f"Los sueldos del turno de mañana son {sMañana}.\nLos sueldos del turno de tarde son {sTarde}.")