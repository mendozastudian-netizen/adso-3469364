"""
25. Mostrar menú:
 Saludar
 Mostrar fecha (simulada)
 Salir
Solicitar opción y ejecutar.

"""
#opciones
saludo = "hola usuario"
fecha = "10.05-2026"
salida = "salir"

print("OPCIONES")
print("1.saludar")
print("2.fecha")
print("3.salir")

elige_una_opcion = input("elige una opcion: ")

if elige_una_opcion == "1":
    print("¡ey!", saludo)

else:
    if elige_una_opcion == "2":
        print("la fecha del dia de hoy es:", fecha)

    else:
        if elige_una_opcion == "3":
            print("hasta luego usuario")

        else:
            print("esa no es una opcion")
