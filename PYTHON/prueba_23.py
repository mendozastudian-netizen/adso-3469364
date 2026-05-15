"""
Solicitar salario base y horas extra:
 Hora extra = 1.5 * valor hora
Calcular salario total.
"""
"""
salario=int(input("ingrese su salario"))
extra=int(input("ingresar horas extra"))
valor_hora=7959
hora_extra=1.5
total=valor_hora*extra*hora_extra
"""
salario=int(input("ingrese su salario:"))
extra=int(input("ingrese horas extra:"))


if extra<=0:
    print("no a hecho horas extra")
    print("su salario es de:",salario)
else:
    if extra>=16:
     print("usted ya no puede hacer mas horas extra")
    else:
       valor_hora=7959
       hora_extra=1.5
       total=valor_hora*extra*hora_extra+salario
       
       print("su salario mas las horas extra es de:",total)