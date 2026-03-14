try:
    num1 = int(input("Introdueix el primer número: "))
    num2 = int(input("Introdueix el segon número: "))
    resultat = num1 / num2
    print("El resultat de la divisió és:", resultat)
except ZeroDivisionError:
    print("No es pot dividir per zero.")
except ValueError:
    print("Per favor, introdueix valors numèrics vàlids.")
