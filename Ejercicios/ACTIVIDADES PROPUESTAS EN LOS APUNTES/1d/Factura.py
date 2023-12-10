suma=0
numero =2
while numero != 0:
    numero = int(input("Introduce precio para la factura (parará cuando introduzcas 0): "))
    suma+=numero
print (f"Total de factura: {suma:.2f}")