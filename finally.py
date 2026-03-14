try:
    num1 = int(input("Introdueix un número: "))
    num2 = int(input("Introdueix un altre número: "))
    resultat = num1 / num2
except ZeroDivisionError:
    print("No es pot dividir per zero.")
except ValueError:
    print("Per favor, introdueix valors numèrics vàlids.")
else:
    print("El resultat és:", resultat)
finally:
    print("Operació completada.")
