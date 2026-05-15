#Solicitar un número e indicar si es positivo, negativo o cero.
numero=int(input("ingrese un numero:"))
if numero>=1:
    print("este numero es positivo:",numero)
elif numero<=-1:
    print("este numero es negativo:",numero)
else:
    print("este numero es cero","0")
