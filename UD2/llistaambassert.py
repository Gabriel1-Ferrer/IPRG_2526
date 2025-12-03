try:
 elements = ["poma", "pera", "taronja", "plàtan"]
 seleccio = None

 pos = int(input("Introdueix una posició (0-3): "))
except AssertionError:
 print("El numero ha de ser enter. ")
except ValueError:
 print("Introdueix un numero valid. ")
except AssertionError: 
 print("El numero te que estar en el rango entre 0 i 3. ")
finally:
 print("Operació completada. ")

seleccio = elements[pos]
print(f"L'element a la posició {pos} és: {seleccio}")


