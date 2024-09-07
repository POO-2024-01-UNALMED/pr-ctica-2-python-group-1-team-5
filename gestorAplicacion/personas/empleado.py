from gestorAplicacion.personas.persona import Persona
#from gestorAplicacion.establecimientos.funeraria import Funeraria

class Empleado(Persona):
    
    def __init__(self, nombre,cuentaBancaria, jornada, cargo, salario, funeraria, 
                 experiencia=0, trabajosHechos=0):
        super().__init__(nombre, 0, 0,cuentaBancaria)
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

    def getCalificacion(self):
        return self._calificacion

    def setCalificacion(self, calificacion):
        self._calificacion = calificacion

    def getTrabajosHechos(self):
        return self._trabajosHechos

    def setTrabajosHechos(self,trabajosHechos):
        self._trabajosHechos = trabajosHechos

    def isDisponible(self):
        return self._disponible

    def setDisponible(self,disponible):
        if(not self._disponible and disponible):
            self._trabajosHechos += 1
        self._disponible = disponible