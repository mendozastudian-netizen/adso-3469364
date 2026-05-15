"""
    Solicitar tipo de cliente (1=VIP, 2=Normal):
 VIP → 20% descuento

GFPI-F-135 V04

 Normal → 5%
 """
cliente1="vip"
cliente2="ESTANDAR"
print("ELIJA EL TIPO DE CLIENTE")
print("1.VIP")
print("2.NORMAL")
print("3.salir")
#procedimiento

boleta=int(input("ingrese un valor"))
opcion=input("elija una opcion:")
if opcion=="1":

    multiplicacion=boleta*20
    division=multiplicacion/100
    resultado=boleta-division
    print("usted es un ",cliente1,"tiene un descuento del 20%" \
    "su boleta queda en:",resultado)
elif opcion=="2":
    multiplicacion=boleta*5
    division=multiplicacion/100
    resultado=boleta-division
    print("usted es un",cliente2,"tiene un descuento del 5%","su boleta queda en:",resultado)
elif opcion=="3":
    print("hasta luego usuario")
else:
    print("esa no es una opcion")
