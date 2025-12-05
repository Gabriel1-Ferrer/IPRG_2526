nom = input("Introdueix el teu nom: ")
edat = int(input("Introdueix la teua edat: "))
with open('dades_usuari.txt', 'w') as fitxer:
    fitxer.write(nom)
    fitxer.write(str(edat))
