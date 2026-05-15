//Solicitar dos valores e intercambiarlos (mostrar antes y después)

primer_nombre="ivan"
segundo_nombre="alejandro"
console.log("ANTES")
console.log("su primer nombre es:",primer_nombre);
console.log("su segundo nombre es:",segundo_nombre);

let temporal = primer_nombre;

primer_nombre=segundo_nombre;

segundo_nombre=temporal;
console.log("DESPUES");
console.log("su primer nombre es",primer_nombre);
console.log("su segundo nombre es",segundo_nombre);
