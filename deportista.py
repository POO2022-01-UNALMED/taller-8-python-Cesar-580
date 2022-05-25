class Deportista():
    def __init__(self, deporte, añosPracticando):
        self._deporte = deporte
        self._añosPraticando = añosPracticando

    # Métodos get - set
    # Deporte 
    def getDeporte(self):
        return self._deporte
    def setDeporte(self,deporte):
        self._deporte = deporte
    
    #añosPracticando 
    def getAñosPracticando(self):
        return self._añosPraticando
    def setAñosPracticando(self,años):
        self._añosPraticando = años