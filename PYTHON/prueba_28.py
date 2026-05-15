"""
    Solicitar nota (0–5) y clasificar:
 4.5–5 → Excelente
 4–4.49 → Bueno
 3–3.99 → Aprobado
 &lt;3 → Reprobado


    """



excelente=("4,5-5")
bueno=("4,0-4,4")
aprobado=("3,3-3,9")
reprobado=("1,0-3,0")

nota=float(input("ingrese su nota:"))
if nota>=1 and nota<=3.2:
    print("su nota esta entre",reprobado,"su nota es:",nota)
    print("reprobado")
elif nota>=3.3 and nota<=3.9:
    print("su nota esta entre",aprobado,"su nota es:",nota)
    print("aprobado")
elif nota>=4 and nota<=4.4:
    print("su nota esta entre",bueno,"su nota es:",nota)
    print("bueno")

elif nota>=4.5 and nota<=5:
    print("su nota esta entre",excelente,"su nota es:",nota)
    print("excelente")
else:
            nota>=5.1
            print("esa nota es invalida")
