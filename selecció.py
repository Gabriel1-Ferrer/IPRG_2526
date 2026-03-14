while True:
    print("Menú de selecció:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("0. Sortir")

    opcio = input("Selecciona una opció: ")

    if opcio == "1":
        print("Has seleccionat l'Opció 1.")
    elif opcio == "2":
        print("Has seleccionat l'Opció 2.")
    elif opcio == "0":
        print("Sortint del menú...")
        break  
    else:
        print("Opció incorrecta. Torna a intentar-ho.")
