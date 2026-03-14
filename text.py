try:
    text = input("Introdueix un número: ")
    numero = int(text)
    print(f"Has introduït el número {numero}.")
except ValueError:
    print("Error: El valor introduït no és un número vàlid.")
