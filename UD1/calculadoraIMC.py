peso = float(input("Introduce tu peso en kilogramos:"))
altura = float(input("Introduce tu altura en metros:"))

imc = peso / (altura ** 2)

print(f"\nTu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Estado: Inferior al peso saludable.")
elif 18.5 <= imc <= 24.9:
    print("Estado: Peso saludable.")
else:
    print("Estado: Desbordamiento de peso.")