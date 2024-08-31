from typing import List, Optional
from datetime import time
from gestorAplicacion.establecimientos.establecimiento import Establecimiento
from gestorAplicacion.personas.empleado import Empleado
from gestorAplicacion.personas.cliente import Cliente
from gestorAplicacion.inventario.vehiculo import Vehiculo
from gestorAplicacion.financiero.cuentaBancaria import CuentaBancaria
from gestorAplicacion.establecimientos.cementerio import Cementerio
from gestorAplicacion.financiero.factura import Factura
from gestorAplicacion.inventario.tipoVehiculo import TipoVehiculo
from gestorAplicacion.inventario.tumba import Tumba

class Funeraria(Establecimiento):
    _cuentaAhorros: Optional[CuentaBancaria] = None
    
  
    
    

    def __init__(self, nombre: str, cuentaCorriente: CuentaBancaria, cuentaAhorros: CuentaBancaria):
        super().__init__(nombre, cuentaCorriente)
        Funeraria._cuentaAhorros = cuentaAhorros
        _empleados = []
        _vehiculos = []

    def buscarEstablecimientos(self, tipoEstablecimiento: str, cliente: Cliente) -> List[Establecimiento]:
        establecimientosEvaluar = Establecimiento.buscarPorFuneraria(self, tipoEstablecimiento)
        establecimientosDisponibles = []

        for establecimiento in establecimientosEvaluar:
            if (establecimiento.getAfiliacion() == cliente.getAfiliacion() and
                establecimiento.getCapacidad() >= cliente.cantidadFamiliares()):
                establecimientosDisponibles.append(establecimiento)

        return establecimientosDisponibles

    def buscarCementerios(self, tipoCementerio: str, cliente: Cliente) -> List[Establecimiento]:
        cementerios = self.buscarEstablecimientos("cementerio", cliente)
        cementeriosDisponibles = Cementerio.cementerioPorTipo(cementerios, tipoCementerio)
        return cementeriosDisponibles

    def buscarEmpleados(self, jornada: str, cargo: str) -> List[Empleado]:
        disponibles = []

        for empleado in self._empleados:
            if (empleado.getJornada() == jornada and empleado.getCargo() == cargo):
                disponibles.append(empleado)

        return disponibles

    def buscarEmpleadosPorHoras(self, horas: time, cargo: str) -> List[Empleado]:
        if 6 <= horas.hour <= 14:
            jornada = "mañana"
        elif 15 <= horas.hour <= 22:
            jornada = "tarde"
        else:
            jornada = "noche"

        return self.buscarEmpleados(jornada, cargo)

  


    def buscarCliente(self, tipoCementerio: str, adultoNino: str) -> List[Cliente]:
        clientes = []
        cementerios = Cementerio.cementerioPorTipo(
            Establecimiento.buscarPorFuneraria(self, "cementerio"), tipoCementerio)

        for cementerio in cementerios:
            cementerio = Cementerio(cementerio)  # Assume Cementerio is a proper class
            clientes.extend(cementerio.buscarCliente(adultoNino))

        return clientes

    def buscarClientePorId(self, idCliente: int) -> Optional[Cliente]:
        for cliente in self.clientes:
            if cliente.getCC() == idCliente:
                return cliente
        return None

    def asignarVehiculo(self) -> Optional[str]:
        vehiculosDisponibles = ""
        tipoVehiculos = []

        for vehiculo in self._vehiculos:
            if vehiculo.isEstado() and vehiculo.getTipoVehiculo().getFamiliar():
                tipoVehiculos.append(vehiculo.tipoVehiculo)

        for vehiculo in TipoVehiculo:
            cantidadVehiculos = tipoVehiculos.count(vehiculo)
            if cantidadVehiculos > 0:
                vehiculosDisponibles += (f"Nombre: {vehiculo.name} Disponibles ({cantidadVehiculos}) "
                                          f"capacidad - {vehiculo.capacidad}\n")

        if vehiculosDisponibles=="":
            return None
        return vehiculosDisponibles 

    def buscarTipoVehiculo(self, tipoVehiculo: TipoVehiculo) -> Optional[Vehiculo]:
        for vehiculo in self._vehiculos:
            if vehiculo.isEstado() and vehiculo.getTipoVehiculo() == tipoVehiculo:
                vehiculo.setEstado() = False
                return vehiculo
        return None
    
    def identificar_productos_faltantes(funeraria):
        productos_vendidos = Funeraria.calcular_productos_vendidos(funeraria)
        productos_faltantes = []

        for producto in productos_vendidos:
            if producto.getCantidadVendida() < 10:
               productos_faltantes.append(producto)

        return productos_faltantes
    
    def calcular_productos_vendidos(funeraria):
        productos_vendidos = []
        for factura in funeraria.getListadoFacturas():
            for producto in factura.getListaProductos():
                if producto not in productos_vendidos:
                   productos_vendidos.append(producto)
        return productos_vendidos
    
    def agregar_producto(productos_vendidos, nuevo_producto):
    # Recorre la lista de productos vendidos para encontrar si el producto ya existe
        for producto in productos_vendidos:
        # Compara el nombre del producto existente con el nuevo producto
            if producto.getNombre() == nuevo_producto.getNombre():
            # Si el producto ya existe, actualiza la cantidad vendida
               cantidad_actual = producto.getCantidadVendida()
               producto.setCantidadVendida(cantidad_actual + nuevo_producto.getCantidadVendida())
               return productos_vendidos
    
    # Si el producto no existe en la lista, se añade al final de la lista
        productos_vendidos.append(nuevo_producto)
        return productos_vendidos


    def agregarVehiculo(self, vehiculo: Vehiculo) -> None:
        self._vehiculos.append(vehiculo)

    def agregarEmpleado(self, empleado: Empleado) -> None:
        self._empleados.append(empleado)



    def getClientes(self):
        return self._empleados
    def setClientes(self, clientes):
        self._empleados=clientes

    def gestionEntierro(self, cliente, iglesia, estatura: float) -> List['Establecimiento']:
        # Busca cementerios con el tipo "cuerpos" para el cliente dado
        cementerios = self.buscarCementerios("cuerpos", cliente)
        cementeriosFiltrados = []

        # Recorre cada cementerio encontrado
        for cementerio in cementerios:
            auxCementerio = cementerio  # Suponiendo que cementerio es del tipo Cementerio
            # Se crean máximo 3 horarios para cada cementerio
            auxCementerio.generarHoras()

            # Verifica la disponibilidad de tumbas que cumplan con los filtros
            if len(auxCementerio.disponibilidadInventario("tumba", estatura, cliente.getEdad())) > 0:
                cementeriosFiltrados.append(auxCementerio)

        # Si no hay cementerios filtrados, crea una tumba por defecto y añade el primer cementerio
        if len(cementeriosFiltrados) == 0:
            Tumba("default", cementerios[0], estatura, cliente.getEdad())
            cementeriosFiltrados.append(cementerios[0])

        # Recorre cada cementerio filtrado para ajustar horarios y asignar empleados
        for cementerio in cementeriosFiltrados:
            auxCementerio = cementerio
            # Asigna la primera hora de evento
            auxCementerio.setHoraEvento(auxCementerio.getHorarioEventos()[0])
            # Busca el empleado para la hora de evento
            empleado = self.buscarEmpleadosPorHoras(auxCementerio.getHoraEvento(), "sepulturero")[0]
            auxCementerio.setEmpleado(empleado)
            # Asigna la iglesia
            auxCementerio.setIglesia(iglesia)

        return cementeriosFiltrados
    
    def gestionarTransporte(self, cliente, vehiculos: List['Vehiculo'], hora: time) -> str: 
        familiares = list(cliente.getFamiliares()) 
        conductores = self.buscarEmpleadosPorHoras(hora, "conductor")
        gestionTransporte = f"Resumen de su transporte - Hora de llegada transporte: {hora}\n"

        indice = 1
        while familiares and vehiculos:
            vehiculoAsignar = vehiculos[0]
            pasajeros = vehiculoAsignar.agregarPasajeros(familiares)

            vehiculoAsignar.setConductor(conductores[0])

            gestionTransporte += f"\nVehiculo [{indice}] "
            gestionTransporte += vehiculoAsignar.productoVehiculo(familiares) + "\n"

            gestionTransporte += f"Conductor: {vehiculoAsignar.getConductor()}"

            if len(conductores) > 1:
                conductores.pop(0)

            familiares = [familiar for familiar in familiares if familiar not in pasajeros]
            vehiculoAsignar.setEstado(True)
            vehiculos.pop(0)
            indice += 1

        return gestionTransporte

    def getEmpleados(self):
        return self._empleados
    def setEmpleados(self,empleados):
        self._empleados=empleados
    def getVehiculos(self):
        return self._vehiculos
    def setVehiculos(self,vehiculos):
        self._vehiculos=vehiculos
    