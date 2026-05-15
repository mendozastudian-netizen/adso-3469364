#Solicitar tres números y mostrarlos en orden ascendente.
numer1=int(input("ingresa un numero:"))
numer2=int(input("ingresa un numero:"))
numer3=int(input("ingresa un numero:"))

if numer1<=numer2:
    if numer2<=numer3:
        print(numer1,numer2,numer3)

    else:
        if numer1<=numer3:
          print(numer1,numer3,numer2)  
        else:
            print(numer3,numer1,numer2)
else:
    if numer1<=numer3:
        print(numer2,numer1,numer3)
    else:
        print(numer3,numer2,numer1)
