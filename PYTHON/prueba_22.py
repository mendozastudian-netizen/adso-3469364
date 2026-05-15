#Solicitar tres lados e indicar tipo de triángulo (equilátero, isósceles, escaleno).
lado1=int(input("ingrese un lado"))
lado2=int(input("ingresar un lado"))
lado3=int(input("ingresar un lado"))
if lado1==lado2==lado3:
    
    print("todos los lados son iguales el tipo de triangulo es equilatero")
else:

    if lado1==lado2 or lado1==lado3 or lado2==lado3:
   
        print("dos lados iguales uno diferente diferente el tipo de triangulo es isoceles")
    else:
    
        print("todos sus lados son distintos el tipo de triangulo escaleno")