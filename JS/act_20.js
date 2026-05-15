//Solicitar usuario y contraseña definidos con anterioridad y.
//Validar con lo que ingresa el usuario


let registro = "alejandross";
let contrasena = "goku12234";

let ingreso = "alejandross";
let validacion = "goku12234";

let usuarioCorrecto = ingreso == registro;
let claveCorrecta = validacion == contrasena;

if (usuarioCorrecto && claveCorrecta) {
    console.log("Acceso correcto");
}

else {
    if (!usuarioCorrecto) {
        console.log("usuario incorrecto");
    }

    if (!claveCorrecta) {
        console.log("contraseña incorrecta");
    }

    console.log("ingrese de nuevo");
}