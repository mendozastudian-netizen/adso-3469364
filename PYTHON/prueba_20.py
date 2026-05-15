#Solicitar usuario y contraseña definidos con anterioridad y.
# Validar con lo que ingresa el usuario

registro = "alejandross"
contrasena="goku12234"

ingreso=str(input("ingrese el usuario:"))
validacion=str(input("ingrese la contraseña:"))
if ingreso==registro and validacion==contrasena :
    print("su usuario es correcto:",registro)
    print("su contraseña es correcta:",contrasena)
elif validacion!=contrasena:
    print("su contraseña es incorrecta:")
    print("ingrese de nuevo")
else:
    print("el usuario o la clave son incorrectos:")