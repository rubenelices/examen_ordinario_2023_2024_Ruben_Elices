class Planeta:
    def __init__(self, nombre, volumen):
        self.nombre = nombre
        self.volumen = volumen

class EstrellaDeLaMuerte:
    def __init__(self):
        self.puntos_de_vida = 1000

# EstrellaDeLaMuerte.py

class EstrellaDeLaMuerte:
    def __init__(self):
        self.puntos_de_vida = 1000
        self.naves_aliadas = []

    def agregar_nave_aliada(self, nave_aliada):
        self.naves_aliadas.append(nave_aliada)

    def atacar_nave_aliada(self, nave_aliada):
        if nave_aliada.puntos_vida <= self.puntos_de_vida:
            print(f"La Estrella de la Muerte ha destruido la nave aliada {nave_aliada.nombre}.")
            self.puntos_de_vida -= nave_aliada.puntos_vida
        else:
            print(f"No se puede destruir la nave aliada {nave_aliada.nombre}. Puntos de vida insuficientes.")


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

class Planeta:
    def __init__(self, nombre, volumen,clasificacion):
        self.nombre = nombre
        self.volumen = volumen
        self.clasificacion = clasificacion

from naves import NavePequena
from naves import NaveGrande
# Crear instancias de la Estrella de la Muerte, una NavePequena y una NaveGrande
#No se porque no se importa bien desde el archivo naves.py y me da fallo.
estrella_muerte = EstrellaDeLaMuerte()
nave_pequena = NavePequena("nave pequena", 50)
nave_grande = NaveGrande("nave grande", 150)

# Agregar naves aliadas a la Estrella de la Muerte
estrella_muerte.agregar_nave_aliada(nave_pequena)
estrella_muerte.agregar_nave_aliada(nave_grande)

# Atacar naves aliadas
estrella_muerte.atacar_nave_aliada(nave_pequena)
estrella_muerte.atacar_nave_aliada(nave_grande)

