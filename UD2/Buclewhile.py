contador = 0 
numero = int(input("Introduce un número, si introduces el 0 el programa finalizará: "))

while numero != 0:
    if numero > 0:
        contador += 1
    
    numero = int(input("Introduce un número, si introduces el 0 el programa finalizará: "))

    print("Has introducit", contador, "números positius")