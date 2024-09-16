#from gestorAplicacion.personas.cliente import Cliente
from gestorAplicacion.establecimientos.crematorio import Crematorio
from gestorAplicacion.establecimientos.cementerio import Cementerio
#from gestorAplicacion.establecimientos.establecimiento import Establecimiento
from datetime import time

class Producto():
    
    _productos=[]

    def __init__(self, nombre="", precio=0, cantidad=0, cantidadVendida= 0, establecimiento = None, vehiculo = None, urna = None, tumba = None):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad
        self._cantidadVendida = cantidadVendida
        self._establecimiento = establecimiento
        self._vehiculo = vehiculo
        self._urna = urna
        self._tumba = tumba
        Producto._productos.append(self)
        if self._vehiculo != None:
            self._precio = vehiculo.getTipoVehiculo().getPrecio()
            self._nombre = vehiculo.getTipoVehiculo().name
            self._cantidad = 1


    
    def evento(self, cliente) :
        concepto = None
        hora = self._establecimiento.getHoraEvento() if self._establecimiento else time(0, 0)
        nombreIglesia = self._establecimiento.getIglesia().getNombre() if self._establecimiento and self._establecimiento.getIglesia() else ''
        familiares = ""
        
        if isinstance(self._establecimiento, Crematorio):
            concepto = "Cremación"
        elif isinstance(self._establecimiento, Cementerio):
            cementerio = self._establecimiento
            if cementerio.getTipo() == "cuerpos":
                concepto = "Entierro"
        else:
            concepto = "Entierro de cenizas"
        
        for familiar in cliente.getFamiliares():
            familiares += str(familiar) + "\n"
        
        evento = (
            f"Asunto: Invitación a la Ceremonia de {concepto} de {cliente}\n"
            f"Invita\n{familiares}\n"
            f"Hora de la Ceremonia: {hora}\n"
            f"Lugar de {concepto}: {self._establecimiento.getNombre() if self._establecimiento else ''}\n"
            f"Centro religioso: {nombreIglesia}"
        )
        return evento
    
    # Getters para atributos de instancia
    def getNombre(self):
        return self._nombre

    def getPrecio(self):
        return self._precio

    def getCantidad(self):
        return self._cantidad

    def getCantidadVendida(self):
        return self._cantidadVendida

    def getEstablecimiento(self):
        return self._establecimiento

    def getVehiculo(self):
        return self._vehiculo

    def getUrna(self):
        return self._urna

    def getTumba(self):
        return self._tumba

    # Setters para atributos de instancia
    def setNombre(self, nombre):
        self._nombre = nombre

    def setPrecio(self, precio):
        self._precio = precio

    def setCantidad(self, cantidad):
        self._cantidad = cantidad

    def setCantidadVendida(self, cantidadVendida):
        self._cantidadVendida = cantidadVendida

    def setEstablecimiento(self, establecimiento):
        self._establecimiento = establecimiento

    def setVehiculo(self, vehiculo):
        self._vehiculo = vehiculo

    def setUrna(self, urna):
        self._urna = urna

    def setTumba(self, tumba):
        self._tumba = tumba

    # Getters para atributo de clase
    @classmethod
    def getProductos(cls):
        return cls._productos

    # Setters para atributo de clase
    @classmethod
    def setProductos(cls, productos):
        cls._productos = productos