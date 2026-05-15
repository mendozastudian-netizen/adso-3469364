//Calcular impuesto de ingresos:
//  Si gana nemos de 1.500.000 → 0%
// Entre 1.500.000 y 3.000.000 → 10%
// Mas de 3.000.000 → 20%
// Mostrar salario, impuesto y neto.

ingresos=3000000
let salario=ingresos
console.log("su salario es de:",salario);
if (ingresos < 1500000){
        let impuesto=0;
        console.log("su impuesto seria de:",impuesto);
        console.log("su ingreso neto es de",ingresos);
}
else if (ingresos >= 1500000 || ingresos <= 3000000){ 
        //procedimiento
    let multiplicacion=ingresos*10;
    let division=multiplicacion/100;
    let resultado=ingresos-division;
    console.log("su impuesto seria de:",division);
    console.log("su ingreso neto es de:",resultado);
}
else{
      let multiplicacion=ingresos*20;
      let division=multiplicacion/100;
      let resultado=ingresos-division;
      
      console.log("su impuesto seria de:",division);
      console.log("su ingreso neto es de:",resultado);
}