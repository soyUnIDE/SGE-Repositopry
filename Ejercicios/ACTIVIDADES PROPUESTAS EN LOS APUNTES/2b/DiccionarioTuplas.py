personas={}
for i in range(4):
    dni=input("Introduce tu DNI: ")
    calle=input("Introduce tu calle: ")
    puerta=int(input("Introduce tu número puerta: "))
    piso=int(input("Introduce tu número piso: "))
    personas[dni]=(dni,calle,puerta,piso)
dniaux=input("Introduce el DNI a buscar: ")
if dniaux in personas:
    print(f"La persona con DNI {personas[dniaux][0]} vive en la calle {personas[dniaux][1]}, en la puerta {personas[dniaux][2]} y en el piso {personas[dniaux][3]}.")
else:
    print(f"La persona con DNI {dniaux} no se encuentra almacenada.")