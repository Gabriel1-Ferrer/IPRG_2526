import json

dades_noves = {"nom": "Ferran", "edat": "21", "nota": "8.2", "Assignatures": "Castella, Valencia"}
with open('estudiants.json', 'w') as fitxer:
    json.dump(dades_noves, fitxer, indent=4)
with open('estudiants.json', 'r') as fitxer:
    dades = json.load(fitxer)

dades_recents = {"nom": "Claudia", "edat": "20", "nota": "6.3", "Assignatures": "Matemàtiques, Física"}
with open('estudiants.json', 'w') as fitxer:
    json.dump(dades_recents, fitxer, indent=8)

import csv

dades =[["nom", "edat", "nota", "Assignatures"], ["Ferran", "21", "8.8" "Castellà", "Valencià"], ["Claudia", "20", "6.3", "Matemàtiques", "Física"]]
with open('estudiants.csv', 'w') as fitxer:
    escriptor_csv = csv.writer(fitxer)
    escriptor_csv.writerows(dades)

with open('estudiants.csv', 'r') as fitxer:
    lector_csv = csv.reader(fitxer)
    for fila in lector_csv:
        print(fila)
