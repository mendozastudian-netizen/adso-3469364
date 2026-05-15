#Solicitar dos valores e intercambiarlos (mostrar antes y después)
primer_nombre=str(input("ingrese su primer nombre"))
segundo_nombre=str(input("ingrese su segundo nombre"))
print("su primer nombre es:",primer_nombre)
print("su segundo nombre es:",segundo_nombre)

primer_nombre, segundo_nombre = segundo_nombre, primer_nombre
print("su primer nombre es",primer_nombre)
print("su segundo nombre es",segundo_nombre)


