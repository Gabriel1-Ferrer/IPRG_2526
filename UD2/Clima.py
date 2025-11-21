num = int(input("Introdueix un número: "))
nuvolat = (input("Digues si esta nuvol: "))


print(nuvolat)
if nuvolat.lower()=="s" or nuvolat.lower() == "si": 
    nuvolat= True
else:
    nuvolat= False

if num < 0: 
    print("Fa un fred polar!")
elif num >= 0 and num <= 15:
    if nuvolat == True:
        print("Fa fresquet i el dia esta trist")
    elif nuvolat == False:
        print("Fa fresquet però el sol alegra el día")    

if num >= 16 and num <=25:
    if nuvolat == True:
        print("Temperatura agradable, però potser ploga")
    elif nuvolat == False:
        print("Dia perfecte per eixir a passejar!")

if num >= 26 and num <= 35:
    print("Fa calor, millor buscar ombra")

if num > 35:
    if nuvolat == True:
        print("Calor i humitat... una combinació infernal!")
    elif nuvolat == False:
        print("Fa una calor que fon les pedres!")     
