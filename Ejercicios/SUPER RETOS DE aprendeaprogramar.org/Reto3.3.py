miLista=list(map(int, input().split()))
numero=miLista[0]
veces=miLista[1]
for i in range(1,veces+1):
	cadena=str(numero)+" x "+str(i)+" = "+str(numero*i)
	print(cadena)