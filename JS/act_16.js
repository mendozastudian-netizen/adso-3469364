//Solicitar valor de compra y aplicar descuento:
// 100.000 o mas → 10%
// Menos de 100.000 → sin descuento


    

let valor_compra=100000
if (valor_compra>=100000){
    //procedimiento
    let multiplicacion=valor_compra*10;
    let division=multiplicacion/100;
    let resultado=valor_compra-division;
    
    console.log("su prodcuto tiene un descuento del diez porciento " ,"el precio final es de:",resultado);
}
else{
    console.log("a su producto no se le aplica el descuento","el precio final es de:",valor_compra);
}