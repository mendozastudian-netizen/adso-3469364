#Declarar una variable llamada numero con valor 10 e imprimirla
numero=10
print("10")

#Solicitar dos números enteros y mostrar su suma.
num1=int(input("ingrese un numero:")) 
num2=int(input("ingrese un numero:")) 

suma=num1+num2
print ("la suma es:", suma )

#Solicitar dos números y mostrar: suma, resta, multiplicación y división si el divisor es 0, mostrar mensaje de error
nume1=int(input("ingrese un numero:")) 
nume2=int(input("ingrese un numero:")) 

Suma=nume1+nume2
Resta=nume1-nume2
Multiplicacion=nume1*nume2


print ("la suma es:", Suma )
print ("la resta es:", Resta)
print ("la multiplicacion es:", Multiplicacion)

if nume2 !=0:
    Division=nume1/nume2
    print("la division es:", Division)
else:
    print("no se puede dividir entre cero")
