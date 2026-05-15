#Solicitar año e indicar si es bisiesto.
"""
ano=int(input("ingrese el año:"))
if ano%4==0:
    print("este año es un año bisiesto:",ano)
else:
    if ano%100:
        print("este año es bisiesto:",ano)
    else:
        if ano%400:
            print("este es un año bisiesto:")
        else:
            print("este no es un año bisiesto")
 """
ano=int(input("ingrese el año:"))
if ano%4==0:
    

    if ano%100==0:
        
    
        if ano%400==0:
            print("este es un año bisiesto:",ano)
        else:
            print("este no es un año bisiesto")
    else:
        print("este año es un año bisiesto")
else:
    print("este año no es un año bisiesto")