//Validar acceso:
// usuario = "admin"
// contraseña = "1234"
// rol = "admin"
// Debe cumplir los tres.
let usuario = "alejandross";
let contraseña = "1234";
let rol_correcto = "admin";

let ingreso = prompt("Ingrese su usuario:");
let validacion = prompt("Ingrese su contraseña:");
let rol = prompt("Ingrese su rol:");

if (ingreso === usuario) {

    console.log("El usuario", usuario, "es correcto");

    if (validacion === contraseña) {

        console.log("La contraseña", contraseña, "es correcta");

        if (rol === rol_correcto) {
            console.log("Bienvenido admin:", usuario);
        } 
        else {
            console.log("Error rol:", rol);
        }

    } 
    else {
        console.log("Error contraseña:", validacion);
    }

} 
else {
    console.log("Error usuario:", ingreso);
}