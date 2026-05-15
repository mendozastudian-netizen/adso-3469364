#Solicitar tres números e indicar el mayor.
numer1=int(input("ingresa un numero:"))
numer2=int(input("ingresa un numero:"))
numer3=int(input("ingresa un numero:"))

if numer1>numer2 and numer1>numer3:
    print("el numero mayor es",numer1)
elif numer2>numer1 and numer2>numer3:
    print("el nuemero mayor es",numer2)
else:
    print("el numero mayor es",numer3)