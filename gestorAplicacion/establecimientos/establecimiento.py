import random
from typing import List, Optional
from datetime import time

from gestorAplicacion.establecimientos.funeraria import Funeraria
from gestorAplicacion.establecimientos.cementerio import Cementerio
from gestorAplicacion.establecimientos.crematorio import Crematorio
from gestorAplicacion.personas.cliente import Cliente
from gestorAplicacion.personas.empleado import Empleado
from personas import Persona

class Establecimiento:
    _establecimientos = []

    def __init__(self, nombre, capacidad=0, cuentaCorriente=None, afiliacion=None, empleado=None, funeraria=None, calificacion= 5.0):
        self._nombre = nombre
        self._capacidad = capacidad
        self._cuentaCorriente = cuentaCorriente
        self._afiliacion = afiliacion
        self._jefe = empleado
        self._funeraria = funeraria
        self._calificacion = calificacion
        self.clientes = []
        self._empleados = []
        self._vehiculos = []
        self.horarioEventos = []
        self._descripcionCalificacion = None
        self._vehiculosEnVenta = []
        self._horaEvento = None
        self._iglesia = None
        self._listadoProveedoresVehiculos = []
        self._listadoProveedoresEmpleados = []
        self._productos = []
        self._listadoProveedores = []

        Establecimiento.establecimientos.append(self)

    @staticmethod
    def filtrarEstablecimiento(cls, tipo):
        filtrados = []
        for establecimiento in Establecimiento._establecimientos:
            if tipo == "cementerio" and isinstance(establecimiento, Cementerio):
                filtrados.append(establecimiento)
            elif tipo == "crematorio" and isinstance(establecimiento, Crematorio):
                filtrados.append(establecimiento)
            elif tipo == "funeraria" and isinstance(establecimiento, Funeraria):
                filtrados.append(establecimiento)
        return filtrados

    @staticmethod
    def buscarPorFuneraria(funeraria, tipoEstablecimiento) -> List['Establecimiento']:
        establecimientosFuneraria = []
        establecimientosEvaluar = Establecimiento.filtrarEstablecimiento(tipoEstablecimiento)
        for establecimiento in establecimientosEvaluar:
            if establecimiento.funeraria == funeraria:
                establecimientosFuneraria.append(establecimiento)
        return establecimientosFuneraria


    def buscarCliente(self, adultoNino) -> List['Cliente']:
        clientesEdad = []
        if adultoNino == "adulto":
            for cliente in self.clientes:
                if cliente.getCC() != 0:
                    clientesEdad.append(cliente)
        else:
            for cliente in self.clientes:
                if cliente.getCC() == 0:
                    clientesEdad.append(cliente)
        return clientesEdad




    def agregarCliente(self, cliente):
        self.clientes.append(cliente)

    def eliminarCliente(self, cliente):
        self.clientes.remove(cliente)



    def buscarClientePorCc(self, cc):
        funerarias = Establecimiento.filtrarEstablecimiento("funeraria")
        cementerios = Establecimiento.filtrarEstablecimiento("cementerio")
        cliente = None

        for funeraria in funerarias:
            for clienteAux in funeraria.buscarCliente("adulto"):
                if clienteAux.getCC() == cc:
                    return clienteAux

        for cementerio in cementerios:
            for clienteAux in cementerio.buscarCliente("adulto"):
                if clienteAux.getCC() == cc:
                    return clienteAux

        return cliente

    def agregarVehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def generarHoras(self):
        if not self.horarioEventos:
            cargo = None
            horaMin = 0
            horaMax = 0

            if isinstance(self, Crematorio):
                cargo = "cremador"
            elif isinstance(self, Cementerio):
                cargo = "sepulturero"

            if self._funeraria.buscarEmpleados("mañana", cargo):
                horaMin = 6
                horaMax = 14
            elif self.funeraria.buscarEmpleados("tarde", cargo):
                if horaMin == 0:
                    horaMin = 15
                horaMax = 22
            elif self._funeraria.buscarEmpleados("noche", cargo):
                if horaMin == 0:
                    horaMax = 30
                    horaMin = 23
                elif horaMin == 15:
                    horaMax = 30
                elif horaMax == 14:
                    horaMin = 23
                    horaMax = 38
                else:
                    horaMin = 0
                    horaMax = 23

            for i in range(3):
                horas = random.randint(horaMin, horaMax)
                minutos = random.randint(0, 59)
                horaGenerada = f"{horas:02d}:{minutos:02d}"
                self.horarioEventos.append(horaGenerada)

    def agregarIglesia(self, iglesia):
        self.iglesia = iglesia

    def eliminarHorario(self, hora):
        self.horarioEventos.remove(hora)


    def __str__(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setCuentaCorriente(self, cuentaCorriente):
        self._cuentaCorriente = cuentaCorriente

    def getCuentaCorriente(self):
        return self._cuentaCorriente

    def setAfiliacion(self, afiliacion):
        self._afiliacion = afiliacion

    def getAfiliacion(self):
        return self._afiliacion

    def setCapacidad(self, capacidad):
        self._capacidad = capacidad

    def getCapacidad(self):
        return self._capacidad

    def setFuneraria(self, funeraria):
        self._funeraria = funeraria

    def getFuneraria(self):
        return self._funeraria

    def getClientes(self):
        return self.clientes

    def setEmpleado(self, empleado):
        self._jefe = empleado

    def getEmpleado(self):
        return self._jefe

    def setCalificacion(self, calificacion: float):
        self._calificacion = calificacion

    def getCalificacion(self):
        return self._calificacion

    def getEmpleados(self):
        return self._empleados

    def agregarEmpleado(self, empleado):
        self._empleados.append(empleado)

    def setHorarioEventos(self, horarioEventos):
        self.horarioEventos = horarioEventos

    def getHorarioEventos(self):
        return self.horarioEventos

    def setHoraEvento(self, horaEvento):
        self.horaEvento = horaEvento

    def getHoraEvento(self):
        return self.horaEvento

    def setIglesia(self, iglesia):
        self._iglesia = iglesia

    def getIglesia(self):
        return self._iglesia

    def getVehiculos(self) :
        return self._vehiculos

    def setVehiculos(self, vehiculos):
        self._vehiculos = vehiculos

    def setClientes(self, clientes):
        self.clientes = clientes

    def setEmpleados(self, empleados):
        self._empleados = empleados

    def setHorarioEventos(self, horarioEventos: List[str]):
        self.horarioEventos = horarioEventos

    