//Solicitar tres números y mostrarlos en orden ascendente.
numer1=4
numer2=16
numer3=1

if (numer1 <= numer2) {

    if (numer2 <= numer3) {
        console.log(numer1, numer2, numer3);
    } 
    else {

        if (numer1 <= numer3) {
            console.log(numer1, numer3, numer2);
        } 
        else {
            console.log(numer3, numer1, numer2);
        }

    }

} 
else {

    if (numer1 <= numer3) {
        console.log(numer2, numer1, numer3);
    } 
    else {
        console.log(numer3, numer2, numer1);
    }

}