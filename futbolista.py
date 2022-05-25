from deportista import Deportista
from persona import Persona

class Futbolista(Deportista):
    _listaFutbolistas=[]

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista._listaFutbolistas.append(self)
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)
    
    # Métodos get set
    # Goles Marcados
    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    # TarjetasRojas
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    # Pierna Habil 
    def getPiernaHabil(self):
        return self._piernaHabil
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil


    # Métodos
    def __str__(self):
        return "Mi nombre es "+self.getNombre()+" soy profesional en el deporte "+self.getDeporte()+" Tengo "+str(self.getEdad())+" años de edad y llevo "+str(self.getAñosPracticando()) +" años en el deporte"   

