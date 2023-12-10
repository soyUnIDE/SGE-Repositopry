sueldo=int(input("Introduce el tu sueldo: "))
años=int(input("Introduce tus años de antiguedad en la empresa: "))
if sueldo<500 and años>=10:
    print(f"Tu nuevo sueldo es de {sueldo+(sueldo*0.2)}€/mes.")
elif sueldo<500 and años<10:
    print(f"Tu nuevo sueldo es de {sueldo+(sueldo*0.05)}€/mes.")
elif sueldo>=500:
    print(f"Tu sueldo se queda igual en {sueldo}€/mes.")