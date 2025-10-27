# Calcular comisiones
# Preguntar nombre de trabajador y cuanto han vendido, les da el 13% de comision
# Responder con frase:   Ok {trabajador_nombre}. Este mes ganaste {total}
#total = venta*1.13

nombre_empleado = input("Dame tu nombre: ")
venta_empleado = input("Cuanto vendiste este mes: ")

total = float(venta_empleado)*.13

print(f"Ok {nombre_empleado}. Este mes ganaste ${round(total)} en comisiones.")

