suma = 0
while True:
    num = int(input("Introdueix un número: "))
    if num < 0:
        break  
    suma += num
print("La suma dels números introduïts és:", suma)
