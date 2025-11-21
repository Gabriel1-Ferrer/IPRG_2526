print("Classificador d'alumnes per edat i assistència")

n = int(input("Quants alumnes vols processar? "))
i = 1

while i <= n:
    nom = input("Nom: ")
    edat = int(input("Edat: "))
    assist = input("Assistència (S/N): ").lower()

    if edat < 12:
        categoria = print("infantil")
    elif edat > 12 and edat < 18:
        categoria = print("adolescent")
    elif edat >= 18 and edat < 65:
        categoria = print("adult")
    else:
        categoria = print("jubilat")
    
    if assist == "s" or "si":
        estat = print("present")
    else:
     estat = print("absent")

     print(nom, "-", categoria, "-", estat)
    i = i + 1
