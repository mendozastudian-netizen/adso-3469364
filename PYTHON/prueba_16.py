"""
Solicitar valor de compra y aplicar descuento:
 100.000 o mas → 10%
 Menos de 100.000 → sin descuento
"""
valor_compra=float(input("el producto tiene un precio de:"))
if valor_compra>=100000:
    #procedimiento
    multiplicacion=valor_compra*10
    division=multiplicacion/100
    resultado=valor_compra-division
    
      
    
    print("su prodcuto tiene un descuento del diez porciento " \
    "el precio final es de:",resultado)
else:
    print("a su producto no se le aplica el descuento" \
          "el precio final es de:",valor_compra)