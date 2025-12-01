try: 
 elements = ["poma", "pera", "taronja", "plàtan"]
 seleccio = None

 pos = int(input("Introdueix una posició (0-3): "))
except AssertionError: 
 print("Tens que introduir un número enter.")
except AssertionError: 
 print("El numero no existeix") 
except ValueError: 
 print("Tens que introduir un numero del 0 al 3.")
 print("Intent completat.") 
seleccio = elements[pos]
print(f"L'element a la posició {pos} és: {seleccio}")
 
print("La longitud de la llista es: 4")
print(f"Selecció reiniciada a {None}")

