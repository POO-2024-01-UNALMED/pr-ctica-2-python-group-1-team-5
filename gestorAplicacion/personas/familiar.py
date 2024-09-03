
from gestorAplicacion.personas.persona import Persona


class Familiar(Persona):
    def __init__(self, nombre, cc=0, edad=0, cuentaBancaria=None, 
                 parentesco=None, acompañantes=0, responsable=None):
        super().__init__(nombre, cc if cc is not None else 0, edad, cuentaBancaria)
        self._parentesco = parentesco
        self._acompañantes = acompañantes if acompañantes is not None else 0
        self._responsable = responsable



    def __str__(self):
        return f"{self._parentesco.upper()} {self.getNombre()}"

    # Métodos get y set
    def getParentesco(self):
        return self._parentesco

    def setParentesco(self, parentesco):
        self._parentesco = parentesco

    def getAcompañantes(self):
        return self._acompañantes

    def setAcompanantes(self, acompañantes: int):
        self._acompañantes = acompañantes

    def getResponsable(self):
        return self._responsable

    def setResponsable(self, responsable):
        self._responsable = responsable
