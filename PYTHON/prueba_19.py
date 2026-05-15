"""
Calcular impuesto de ingresos:
 Si gana nemos de 1.500.000 → 0%
 Entre 1.500.000 y 3.000.000 → 10%
 Mas de 3.000.000 → 20%
Mostrar salario, impuesto y neto.
"""
ingresos=float(input("de cuanto son sus ingresos:"))
salario=ingresos
print("su salario es de:",salario)
if ingresos < 1500000:
        impuesto=0
        
        print("su impuesto seria de:",impuesto)
        print("su ingreso neto es de:",ingresos)
elif ingresos >= 1500000 and ingresos <= 3000000: 
        #procedimiento
    multiplicacion=ingresos*10
    division=multiplicacion/100
    resultado=ingresos-division
    print("su impuesto seria de:",division)
    print("su ingreso neto es de:",resultado)
else:
      multiplicacion=ingresos*20
      division=multiplicacion/100
      resultado=ingresos-division
      
      print("su impuesto seria de:",division)
      print("su ingreso neto es de:",resultado)