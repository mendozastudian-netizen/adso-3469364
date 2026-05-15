#Solicitar número del mes (1–12) y mostrar estación (definir claramente las estaciones)
num_mes=int(input("ingrese un mes del año:"))
if num_mes>=3 and num_mes<=5:
    print("en este mes",num_mes,"estamos en primavera")
elif num_mes>=6 and num_mes<=8:
    print("en este mes",num_mes,"estamos en verano")
elif num_mes>=9 and num_mes<=11:
    print("en este mes",num_mes,"estamos en otoño")
elif num_mes in (12,1,2):
    print("en este mes",num_mes,"estamos en invierno")
else:
    print("este mes no existe")
