import csv 

with open('dades_exercici.csv', 'r') as fitxer:
    lector_csv = csv.reader(fitxer) 
    

dades= [["Nom", "Edat", "Curs"], ["Josep", "25", "Valencià"]]
with open('dades_exercici.csv', 'w' newline= ) as fitxer:
    escriptor_csv = csv.writer(fitxer)
    escriptor_csv.writerows(dades)