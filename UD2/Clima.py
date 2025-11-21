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


