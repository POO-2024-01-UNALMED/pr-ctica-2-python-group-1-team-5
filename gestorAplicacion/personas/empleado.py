from gestorAplicacion.personas.persona import Persona
#from gestorAplicacion.establecimientos.funeraria import Funeraria

class Empleado(Persona):

    def __init__(self, nombre, CC,edad,cuentaBancaria, jornada, cargo, salario=0, 
                 experiencia=0, trabajosHechos=0, funeraria=None):
        super().__init__(nombre, CC, edad,cuentaBancaria)
        self._jornada = jornada
        self._cargo = cargo
        self._salario = salario
        self._experiencia = experiencia
        self._trabajosHechos = trabajosHechos
        self._disponible = True
        self._descripcionCalificacion = ""
        self._calificacion = 5
        self._funeraria = funeraria
        
        if funeraria is not None:
            funeraria.agregarEmpleado(self)


    def getCargo(self):
        return self._cargo

    def setCargo(self, cargo):
        self._cargo = cargo

    def getJornada(self):
        return self._jornada
    
    def setJornada(self, jornada):
        self._jornada = jornada