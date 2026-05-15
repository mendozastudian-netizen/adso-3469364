//Solicitar edad y clasificar:
//  0 o 12 niño
// 13 o 17 joven
// 18 o 59 adulto
// 60 o mas adulto mayor

edad=65
if (edad >=0 && edad<=12){
    console.log("usted es un niño de:",edad);
}
else if (edad >=13 && edad<=17){
    console.log("usted es un joven de:",edad);
}
else if (edad >=18 && edad<=59){
    console.log("usted es un adulto de:",edad);
}
else{
     console.log("usted es un adulto mayor de",edad);
}