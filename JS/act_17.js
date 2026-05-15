//Solicitar un número e indicar si es múltiplo de 5.

numero=45
if (numero<=0){
    console.log("numero invalido");
}
else if (numero%5==0){
    console.log("el numero ingresado es multiplo de 5:",numero);
}
else{
    console.log("el numero ingresado no es multiplo de 5:",numero);
}