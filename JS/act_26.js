//    Solicitar tipo de cliente (1=VIP, 2=Normal):
// VIP → 20% descuento
// GFPI-F-135 V04
// Normal → 5%

cliente1="vip"
cliente2="ESTANDAR"
console.log("ELIJA EL TIPO DE CLIENTE");
console.log("1.VIP");
console.log("2.NORMAL");
console.log("3.salir");
//procedimiento

boleta=400000;
opcion= "2";
if (opcion=="1"){

    multiplicacion=boleta*20;
    division=multiplicacion/100;
    resultado=boleta-division;
    console.log("usted es un ",cliente1,"tiene un descuento del 20%" ,"su boleta queda en:",resultado);
}
else if (opcion=="2"){
    multiplicacion=boleta*5;
    division=multiplicacion/100;
    resultado=boleta-division;
    console.log("usted es un",cliente2,"tiene un descuento del 5%","su boleta queda en",resultado);
}
else if (opcion=="3"){
    print("hasta luego usuario");
}
else{
    print("esa no es una opcion");
}