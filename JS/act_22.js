//Solicitar tres lados e indicar tipo de triángulo (equilátero, isósceles, escaleno).

lado1=3
lado2=7
lado3=8

if (lado1==lado2 && lado2==lado3){
    
    console.log("todos los lados son iguales el tipo de triangulo es equilatero");
}
else if (lado1==lado2 || lado1==lado3 || lado2==lado3){
   
        console.log("dos lados iguales uno diferente diferente el tipo de triangulo es isoceles");
    }
    else{
    
        console.log("todos sus lados son distintos el tipo de triangulo escaleno");
    }