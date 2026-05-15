
let ano = 2026

if (ano % 400 == 0) {
    console.log("es bisiesto:", ano);
}

else if (ano % 100 == 0) {
    console.log("no es bisiesto:", ano);
}

else if (ano % 4 == 0) {
    console.log("es bisiesto:", ano);
}

else {
    console.log("no es bisiesto:", ano);
}