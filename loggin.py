import logging

# Configuració de logging
logging.basicConfig(filename='gestio_entrades.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Simulació d'una funció de reserva de seient
def reservar_seient(seient, nom):
    if seient < 1 or seient > 10:
        logging.warning(f"Intent de reserva invàlida: Seient {seient} fora de rang.")
        return "Seient invàlid"
    else:
        logging.info(f"Seient {seient} reservat per {nom}.")
        return f"Seient {seient} reservat correctament per {nom}"

# Prova de reserva
resultat = reservar_seient(5, "Joan")
print(resultat)

# Error a l'intentar reservar un seient invàlid
resultat = reservar_seient(9, "Maria")
print(resultat)
