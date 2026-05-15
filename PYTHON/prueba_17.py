#Solicitar un número e indicar si es múltiplo de 5.
numero=int(input("ingrese un numero:"))
if numero<=0:
    print("numero invalido")
elif numero%5==0:
    print("el numero ingresado es multiplo de 5:",numero)
else:
    print("el numero ingresado no es multiplo de 5:",numero)