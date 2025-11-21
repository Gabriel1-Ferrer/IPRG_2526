contador = 0
numero = int(input("Introdueix un numero si es major de 100 el programa finalitzará: "))

while numero >= 100:
    if numero < 100:
        contador += 1
    
         
    numero = int(input("Introdueix un numero si el major de 100 el programa finalitzará: "))


    print ("Has introduit", contador, "números positius")

    if numero < 100: 
        break

    

