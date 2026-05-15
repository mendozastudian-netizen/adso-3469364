//Solicitar una nota (0 a 5) e indicar:
//El estudiante aprueba con 3.5 o mas

nota=4.6
if (nota<0 || nota>5.0){
    console.log("la nota no es valida");
}
else if (nota>=3.5){
    console.log("usted aprobado esta materia:",nota);
}

else{
    console.log("usted a reprobado esta materia:", nota);
}
