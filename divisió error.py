try:
    num1 = int(input("Introdueix el primer número: "))
    num2 = int(input("Introdueix el segon número: "))

    resultat = num1 / num2 
    print("El resultat es:", resultat)

except ZeroDivisionError:
    print("No se pot dividir entre zero")

except ValueError:
    print("Introdueix numeros valids")

    