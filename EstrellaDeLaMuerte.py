from Planetas import Planeta

class EstrellaDeLaMuerte:
    def __init__(self):
        self.puntos_de_vida = 1000

    def destruir_planeta(self, planeta):
        if isinstance(planeta, Planeta):
            if planeta.volumen <= self.puntos_de_vida:
                print(f"La Estrella de la Muerte ha destruido el planeta {planeta.nombre}.")
                self.puntos_de_vida -= planeta.volumen
                print("La estrella de la muerte se ha quedado con",self.puntos_de_vida,"puntos de vida")
            else:
                print(f"No se puede destruir el planeta {planeta.nombre}. Volumen demasiado alto.")
        else:
            print("El objeto no es una instancia de la clase Planeta.")

# Crear instancias de la Estrella de la Muerte y planetas
estrella_muerte = EstrellaDeLaMuerte()
concordia = Planeta("Concordia", 500)
ilum = Planeta("Ilum", 1200)
kamino = Planeta("Kamino", 800)

# Llamar al método destruir_planeta para cada planeta
estrella_muerte.destruir_planeta(concordia)
estrella_muerte.destruir_planeta(ilum)
estrella_muerte.destruir_planeta(kamino)
