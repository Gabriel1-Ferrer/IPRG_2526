try: 
      import json
      with open('dades_exercici.json', 'r') as fitxer:
       dades = json.load(fitxer)

       dades_noves = {"nom": "Joan", "edat": "25", "nota": "8.5", "assignatures": "matemátiques , física",}
       with open('dades_exercici.json', 'w') as fitxers:
        json.dump(dades_noves, fitxer, indent=4)

except Exception as e:
   print(f"S'ha produit un error inesperat: {e}")
         