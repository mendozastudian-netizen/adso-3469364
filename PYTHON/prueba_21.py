"""
Solicitar edad y clasificar:
 0 o 12 niño
 13 o 17 joven
 18 o 59 adulto
 60 o mas adulto mayor
"""
edad=int(input("ingrese su edad:"))
if edad >=0 and edad<=12 :
    print("usted es un niño de:",edad)
elif edad >=13 and edad<=17:
    print("usted es un joven de:",edad)
elif edad >=18 and edad<=59:
    print("usted es un adulto de:",edad)
else:
    print("usted es un adulto mayor de",edad)