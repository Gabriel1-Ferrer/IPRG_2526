try:
   nom = input("Introdueix el teu nom: ")
   edat = int(input("Introdueix la teua edat: "))
   ciutat = input("Introdueix la teua ciutat en la que vius: ")
   with open('dades_usuari.txt', 'w') as fitxer:
        fitxer.write(nom) 
        fitxer.write(str(edat))
        fitxer.write(ciutat)


except FileNotFoundError:
    print("El fitxer no existeix.")


