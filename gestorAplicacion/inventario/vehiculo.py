class Vehiculo:
    _vehiculos = []

    def __init__(self, tipoVehiculo, funeraria= None, color= None, placa= None, precio= None, capacidad= None):
        self._tipoVehiculo = tipoVehiculo
        self._funeraria = funeraria
        self._color = color
        self._placa = placa
        self._precio = precio
        self._capacidad = capacidad
        self._estado = True  # True si está disponible, False si no lo está
        self._conductor = None
        self._pasajeros = []
        if funeraria != None:
            funeraria.agregarVehiculo(self)
        Vehiculo._vehiculos.append(self)

    def agregarPasajeros(self, familiares):
        familiaresMenores = [f for f in familiares if f.getEdad() < 18]
        familiaresMayores = [f for f in familiares if f.getEdad() >= 18]
        
        pasajeros = []
        capacidad = self._tipoVehiculo.getCapacidad()

        while capacidad > 0:
            if capacidad % 2 == 0 and familiaresMenores:
                familiarMenor = familiaresMenores.pop(0)
                pasajeros.append(familiarMenor)
                if familiarMenor.getResponsable():
                    pasajeros.append(familiarMenor.getResponsable())
                    familiaresMayores.remove(familiarMenor.getResponsable())
                capacidad -= 2
            elif familiaresMayores and capacidad > 0:
                familiarMayor = familiaresMayores.pop(0)
                pasajeros.append(familiarMayor)
                capacidad -= 1
            else:
                break
        
        self._pasajeros = pasajeros
        return pasajeros

    def productoVehiculo(self, pasajeros) -> str:
        producto = f"Vehículo {self._tipoVehiculo} - color: {self._color} - placa: {self._placa}\n"
        for pasajero in pasajeros:
            if pasajero.getCC() == 0:
                producto += f"Familiar menor de edad: {pasajero} Acudiente: {pasajero.getResponsable()}\n"
            else:
                producto += f"Familiar: {pasajero}\n"
        return producto

    def agregarPasajero(self, pasajero):
        self._pasajeros.append(pasajero)
        self._estado = False

    def __str__(self):
        return str(self._tipoVehiculo)

    # Métodos get y set
    @staticmethod
    def getVehiculos():
        return Vehiculo._vehiculos

    def getTipoVehiculo(self):
        return self._tipoVehiculo
    
    def getPlaca(self) -> str:
        return self._placa
    
    def setPlaca(self, placa: str):
        self._placa = placa

    def getConductor(self):
        return self._conductor
    
    def setConductor(self, conductor):
        self._conductor = conductor

    def getRuta(self):
        return self._ruta
    
    def setRuta(self, ruta):
        self._ruta = ruta

    def getPasajeros(self):
        return self._pasajeros

    def getFuneraria(self):
        return self._funeraria
    
    def setFuneraria(self, funeraria):
        self._funeraria = funeraria

    def getColor(self) -> str:
        return self._color
    
    def setColor(self, color):
        self._color = color

    def isEstado(self) -> bool:
        return self._estado
    
    def setEstado(self, estado: bool):
        self._estado = estado

    def setTipoVehiculo(self, tipoVehiculo):
        self._tipoVehiculo = tipoVehiculo

    def setPasajeros(self, pasajeros):
        self._pasajeros = pasajeros

    def getEstado(self) -> bool:
        return self._estado

    def getCapacidad(self) -> int:
        return self._capacidad
    
    def setCapacidad(self, capacidad: int):
        self._capacidad = capacidad

    def getPrecio(self) -> int:
        return self._precio
    
    def setPrecio(self, precio: int):
        self._precio = precio