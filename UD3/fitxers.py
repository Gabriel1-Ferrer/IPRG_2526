with open('prueba.txt', 'x') as fitxer:
    fitxer.write("Primera línia")
with open('prueba.txt', 'w') as fitxer:
    fitxer.write("Segona línia")
with open('prueba.txt', 'a') as fitxer:
    fitxer.write("Quarta línia")
with open('prueba.txt', 'a') as fitxer:
    fitxer.write("Cinquena línia")
    fitxer.write("Sisena línia")
with open('prueba.txt', 'r') as fitxer:
    contingut = fitxer.read()
    print(contingut)

'''
with open('file_not_exist.txt', 'r') as noExisteix:
    print(noExisteix)
'''

with open('prueba.txt', 'r' ) as fitxer:
    contingut = fitxer.read()
    print (contingut)
fitxer.close()
    