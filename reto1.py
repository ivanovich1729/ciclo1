# Solicitar al usuario ingresar el salario base, horas extra y bonificaciones.
salario_base, horas_extra, bonificacion = input().split()
salario_base = float(salario_base)
horas_extra = int(horas_extra)
bonificacion = int(bonificacion)
# Calcular horas extra con un recargo de 45% del valor de una hora.
valor_hora_extra = (salario_base / 180) * 1.45
valor_hora_extra *= horas_extra
# Calcular la bonificacion.
bonificacion *= (salario_base * 0.015)
# Calcular el salario total.
salario_total = salario_base + valor_hora_extra + bonificacion
# Calcular los descuentos. Salud 5.5%, Pensión y Caja 5% antes de descuentos.
descuentos = salario_total * 0.155
salario_recibido = salario_total - descuentos
# Regresar el salario con descuentos y el salario total.
print("{0:.1f}".format(salario_recibido), "{0:.1f}".format(salario_total))