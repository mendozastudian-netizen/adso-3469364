// Mostrar menú:
// Saludar
// Mostrar fecha (simulada)
// Salir
// Solicitar opción y ejecutar.
const prompt = require("prompt-sync")();

let saludo = "hola usuario";
let fecha = "10.05-2026";
let salida = "salir";

console.log("OPCIONES");
console.log("1. saludar");
console.log("2. fecha");
console.log("3. salir");

let elige_una_opcion = "1"

if (elige_una_opcion == "1") {
    console.log("¡ey!", saludo);
}
else {
    if (elige_una_opcion == "2") {
        console.log("la fecha del dia de hoy es:", fecha);
    }
    else {
        if (elige_una_opcion == "3") {
            console.log("hasta luego usuario");
        }
        else {
            console.log("esa no es una opcion");
        }
    }
}