try:
    num1 = int(input("Introdueix el primer número: "))
    num2 = int(input("Introdueix el segon número: "))
    resultat = num1 / num2
    print(f"El resultat de la divisió és: {resultat}")

except ZeroDivisionError:
    print("No es pot dividir per zero.")
except ValueError:
    print("Introdueix els valor numerics valids: ") 

    


