//Solicitar número del mes (1–12) y mostrar estación (definir claramente las estaciones)
num_mes=12
if (num_mes>=3 && num_mes<=5){
    console.log("en este mes",num_mes,"estamos en primavera");
}
else if (num_mes>=6 && num_mes<=8){
    console.log("en este mes",num_mes,"estamos en verano");
}
else if (num_mes>=9 && num_mes<=11){
    console.log("en este mes",num_mes,"estamos en otoño");
}
else if ([12, 1, 2].includes(num_mes)) {
    console.log("En este mes", num_mes, "estamos en invierno");
}
else{
    console.log("este mes no existe");
}