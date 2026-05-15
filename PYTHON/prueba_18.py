"""
Solicitar una nota (0 a 5) e indicar:
 El estudiante aprueba con 3.5 o mas
"""
nota=float(input("ingrese su nota:"))
if nota<0 or nota>5.0:
    print("la nota no es valida")
    
elif nota>=3.5:
    print("usted aprobado esta materia:",nota)

else :
    print("usted a reprobado esta materia:", nota)
