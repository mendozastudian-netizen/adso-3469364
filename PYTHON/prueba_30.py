"""
Validar acceso:
usuario = "admin"
contraseña = "1234"
rol = "admin"
Debe cumplir los tres.
"""
usuario="alejandross"
contraseña="1234"
rol_correcto="admin"

ingreso=str(input("ingrese su usuario: "))
validacion=str(input("ingrese su contraseña: "))
rol=str(input("ingrese su rol:" ))
if ingreso==usuario:
    print("el usuario",usuario,"es correcto")
    if validacion==contraseña:
        print("la contraseña",contraseña,"es correcta")
        if rol==rol_correcto:
            print("bienvenido admin:,",usuario)
        else:
            print("error rol:",rol)
    else:
        print("error contraseña:",validacion)
else:
   print ("error usuario:",ingreso)