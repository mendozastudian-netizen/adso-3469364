//  Solicitar nota (0–5) y clasificar:
// 4.5–5 → Excelente
// 4–4.49 → Bueno
//  3–3.99 → Aprobado
// 1.0-2.9Reprobado

excelente=("4,5-5")
bueno=("4,0-4,4")
aprobado=("3,3-3,9")
reprobado=("1,0-3,0")

nota=3.9

if (nota>=1 && nota<=3.2){
    console.log("su nota esta entre",reprobado,"su nota es:",nota);
    console.log("reprobado");
}
else if (nota>=3.3 && nota<=3.9){
    console.log("su nota esta entre",aprobado,"su nota es:",nota);
    console.log("aprobado");
}
else if (nota>=4 && nota<=4.4){
    console.log("su nota esta entre",bueno,"su nota es:",nota);
    console.log("bueno");
}

else if (nota>=4.5 && nota<=5){
    console.log("su nota esta entre",excelente,"su nota es:",nota);
    console.log("excelente");
}
else{
            nota>=5.1
            console.log("esa nota es invalida");
}