n1=int(input("Introduce la primera nota: "))
n2=int(input("Introduce la segunda nota "))
n3=int(input("Introduce la tercera nota: "))
if n1<4 and n2<4 and n3<4:
    print("La nota final es 0.")
elif n1>4 and n2>4 and n3>4:
    print(f"La nota final es {(n1*0.3)+(n2*0.2)+(n3*0.5)}")
else:
    print("La nota final es 2.")
