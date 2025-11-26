contador = 0
numero = int(input("Introdueix un numero del 1 al 10: "))

for i in  range(10):
    if numero % 2 == 0:
        continue
    else:
        contador+=1

        print("Has imprimit números imparells del 1 al 10.")
