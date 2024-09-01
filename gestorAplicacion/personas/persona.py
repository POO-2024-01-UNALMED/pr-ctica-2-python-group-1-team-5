#from gestorAplicacion.inventario.inventario import *
class Persona:
    _personas = []
    auxCC: int = 1000

    def __init__(self, nombre, CC, edad, cuentaBancaria):
        self._nombre = nombre
        self._CC = CC
        self._edad = edad
        self._cuentaBancaria = cuentaBancaria
        Persona._personas.append(self)
        Persona.auxCC += 1

    @staticmethod
    def getPersonas():
        return Persona._personas

    def __str__(self):
        return self._nombre

    def getNombre(self):
        return self._nombre

    def setNombre(self, value):
        self._nombre = value

    def getCC(self):
        return self._CC

    def getEdad(self):
        return self._edad

    def setEdad(self, value):
        self._edad = value

    def getCuentaBancaria(self):
        return self._cuentaBancaria


    def setCuentaBancaria(self, value):
        self._cuentaBancaria = value