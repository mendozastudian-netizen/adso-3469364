//Solicitar salario base y horas extra
//  Hora extra = 1.5 * valor hora
// Calcular salario total.

salario=1759250
extra=14


if (extra<=0){
    console.log("no a hecho horas extra");
    console.log("su salario es de:",salario);
}
else if (extra>=16){
     console.log("usted ya no puede hacer mas horas extra");
}
    else{
       let valor_hora=7959;
       let hora_extra=1.5;
       let total=valor_hora*extra*hora_extra+salario;
       
       console.log("su salario mas las horas extra es de:",total);
    }