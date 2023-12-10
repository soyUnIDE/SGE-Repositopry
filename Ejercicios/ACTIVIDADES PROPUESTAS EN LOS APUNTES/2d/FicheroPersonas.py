lectura = open("2d/Personas.txt", "r")
lineas = lectura.readlines()
numLinea = 0
personas=[]
for linea in lineas:
    persona = linea.split(";")
    if persona[1].endswith("\n"):
        edad=persona[1].replace("\n","")
        persona[1]=edad
    personas.append(persona)
mayor=0
menor=99999999999999
mayorL=[]
menorL=[]
for p in personas:
    edad=int(p[1])
    if edad>mayor:
        mayorL=p
        mayor=edad
    if edad<menor:
        menorL=p
        menor=edad
print(f"La persona mas mayor es {mayorL[0]} con {mayorL[1]} años.\nLa persona mas joven es {menorL[0]} con {menorL[1]} años.")
