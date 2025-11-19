def saludar(Maite):
    print(f"¡Hola, {Maite}! Bienvenida.")

saludar("Maite")

import math


def area_circulo(radio):
    """Devuelve el área de un círculo dado su radio."""
    return math.pi * radio**2


resultado = area_circulo(10)
print("El area es", resultado)


radio_usuario = float(input("Introduce el radio del círculo: "))

area = area_circulo(radio_usuario)

print(f"El área del círculo es: {area}")

def sumar(a, b=7):
    return a + b

resultado1 = sumar(12)

resultado2 = sumar(12, 5)

print("Resultado con un solo valor:", resultado1)
print("Resultado con dos valores:", resultado2)



