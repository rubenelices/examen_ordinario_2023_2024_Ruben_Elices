from enum import Enum

class Clasificacion(Enum):
    CONCORDIA = 1
    LLUM = 2
    KAMINO = 3

class Planeta:
    def __init__(self, nombre, volumen, clasificacion):
        self.nombre = nombre
        self.volumen = volumen
        self.clasificacion = clasificacion

class PlanetaConcordia(Planeta):
    def __init__(self, nombre, volumen):
        super().__init__(nombre, volumen, Clasificacion.CONCORDIA)

class PlanetaLlum(Planeta):
    def __init__(self, nombre, volumen):
        super().__init__(nombre, volumen, Clasificacion.LLUM)

class PlanetaKamino(Planeta):
    def __init__(self, nombre, volumen):
        super().__init__(nombre, volumen, Clasificacion.KAMINO)
