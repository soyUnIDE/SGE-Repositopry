horas_trabajadas = float(input())
precio_por_hora = float(input())

tarifa_normal = precio_por_hora
tarifa_extra = 1.5 * precio_por_hora
horas_normales = min(horas_trabajadas, 35)
horas_extra = max(horas_trabajadas - 35, 0)

sueldo_bruto = (horas_normales * tarifa_normal) + (horas_extra * tarifa_extra)

impuestos_libres = 500
impuestos_25_percent = 400

if sueldo_bruto <= impuestos_libres:
    impuestos = 0
elif sueldo_bruto <= impuestos_libres + impuestos_25_percent:
    impuestos = 0.25 * (sueldo_bruto - impuestos_libres)
else:
    impuestos = 0.25 * impuestos_25_percent + 0.45 * (sueldo_bruto - impuestos_libres - impuestos_25_percent)
sueldo_neto = sueldo_bruto - impuestos
print("{:.2f}".format(sueldo_neto))
