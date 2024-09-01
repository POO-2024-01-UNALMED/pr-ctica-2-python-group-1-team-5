from enum import Enum

class TipoVehiculo(Enum):
    BERLINA = (4, False, True, 70000)
    CARROZA = (6, True, False, 150000)
    FAETON = (4, False, True, 120000)
    COCHEFUNEBRE = (1, True, False, 80000)
    BUS = (6, False, True, 50000)
    COCHERESPETO = (8, False, True, 75000)
    CUPE = (4, False, True, 65000)
    CAMION = (5, False, False, 69000)

    def __init__(self, capacidad, cliente, familiar, precio):
        self._capacidad = capacidad
        self._cliente = cliente
        self._familiar = familiar
        self._precio = precio

    def __str__(self):
        return f"Vehiculo tipo {self.name} - Capacidad: {self.capacidad}"
    
    #getters 
    
    def getCapacidad(self):
        return self._capacidad
    
    def getCliente(self):
        return self._cliente
    
    def getFamiliar(self):
        return self._familiar
    
    def getPrecio(self):
        return self._precio
    
    #setters

    def setCapacidad(self, capacidad):
        self._capacidad = capacidad
    
    def setCliente(self, cliente):
        self._cliente = cliente
    
    def setFamiliar(self,familiar):
        self._familiar = familiar
    
    def setPrecio(self,precio):
        self._precio = precio


