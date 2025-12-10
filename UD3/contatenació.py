
fitxerslist = ["dades_usuari.txt" ]

with open('fitxercontatenació.txt', 'w') as fitxerAEscriure:
 
  for fitxerOfList in fitxerslist:
    with open(fitxerOfList) as fitxerObert:
      fitxerAEscriure.write(fitxerObert.read())


 

