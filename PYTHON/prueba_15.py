#Solicitar edad e indicar si es mayor o menor de edad.
edad=int(input("ingrese su edad:"))

if edad<=17:
    print("usted es menor de:",edad)
elif edad<=99:
    print("usted es mayor de edad",edad)
else:
    print("usted esta muerto",edad)