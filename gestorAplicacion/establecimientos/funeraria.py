from typing import List, Optional
from datetime import time
from gestorAplicacion.establecimientos.establecimiento import Establecimiento
#from gestorAplicacion.personas.empleado import Empleado
#from gestorAplicacion.personas.cliente import Cliente
#from gestorAplicacion.inventario.vehiculo import Vehiculo
#from gestorAplicacion.financiero.cuentaBancaria import CuentaBancaria
from gestorAplicacion.establecimientos.cementerio import Cementerio
from gestorAplicacion.financiero.factura import Factura
from gestorAplicacion.inventario.tipoVehiculo import TipoVehiculo
from gestorAplicacion.inventario.tumba import Tumba
from gestorAplicacion.personas.familiar import Familiar
class Funeraria(Establecimiento):
    _cuentaAhorros = None
    
  
    
    

    def __init__(self, nombre, cuentaCorriente, cuentaAhorros):
        super().__init__(nombre, cuentaCorriente)
        Funeraria._cuentaAhorros = cuentaAhorros
        _empleados = []
        _vehiculos = []

    def buscarEstablecimientos(self, tipoEstablecimiento: str, cliente):
        establecimientosEvaluar = Establecimiento.buscarPorFuneraria(self, tipoEstablecimiento)
        establecimientosDisponibles = []

        for establecimiento in establecimientosEvaluar:
            if (establecimiento.getAfiliacion() == cliente.getAfiliacion() and
                establecimiento.getCapacidad() >= cliente.cantidadFamiliares()):
                establecimientosDisponibles.append(establecimiento)

        return establecimientosDisponibles

    def buscarCementerios(self, tipoCementerio: str, cliente) -> List[Establecimiento]:
        cementerios = self.buscarEstablecimientos("cementerio", cliente)
        cementeriosDisponibles = Cementerio.cementerioPorTipo(cementerios, tipoCementerio)
        return cementeriosDisponibles

    def buscarEmpleados(self, jornada: str, cargo: str) :
        disponibles = []

        for empleado in self._empleados:
            if (empleado.getJornada() == jornada and empleado.getCargo() == cargo):
                disponibles.append(empleado)

        return disponibles

    def buscarEmpleadosPorHoras(self, horas, cargo) :
        if 6 <= int(horas[:2]) <= 14:
            jornada = "mañana"
        elif 15 <= int(horas[:2]) <= 22:
            jornada = "tarde"
        else:
            jornada = "noche"

        return self.buscarEmpleados(jornada, cargo)

  


    def buscarClienteCementerio(self, tipoCementerio: str, adultoNino: str) :
        clientes = []
        cementerios = Cementerio.cementerioPorTipo(
            Establecimiento.buscarPorFuneraria(self, "cementerio"), tipoCementerio)

        for cementerio in cementerios:
            cementerio = Cementerio(cementerio)  # Assume Cementerio is a proper class
            clientes.extend(cementerio.buscarCliente(adultoNino))

        return clientes

    def buscarClientePorId(self, idCliente) :
        for cliente in self.clientes:
            if int(cliente.getCC()) == int(idCliente):
                return cliente
        return None
    
    def cobroServiciosClientes(cliente):
        for i in range(len(cliente._listadoFacturas) - 1, -1, -1):
            factura = cliente._listadoFacturas[i]
            totalFactura = factura._total
            if (cliente._cuentaBancaria is not None and
                totalFactura <= cliente._cuentaBancaria.obtenerSaldo() and
                cliente._edad >= 18):
                cliente._cuentaBancaria.transaccionCuentaAhorros(totalFactura, Funeraria._cuentaAhorros)
                cliente._listadoFacturas.remove(factura)
            else:
                for persona in cliente.familiares:
                    if isinstance(persona, Familiar):
                        familiar = persona
                        if familiar._parentesco is not None:
                            if (familiar._parentesco == "conyuge" and familiar._edad >= 18 and
                                totalFactura <= familiar._cuentaBancaria.obtenerSaldo()):
                                familiar._cuentaBancaria.transaccionCuentaAhorros(totalFactura, Funeraria._cuentaAhorros)
                                cliente._listadoFacturas.remove(factura)
                        elif (familiar._parentesco in ["hijo", "hija"] and familiar._edad >= 18 and
                                totalFactura <= familiar._cuentaBancaria.obtenerSaldo()):
                                familiar._cuentaBancaria.transaccionCuentaAhorros(totalFactura, Funeraria._cuentaAhorros)
                                cliente._listadoFacturas.remove(factura)
                        elif (familiar._parentesco in ["padre", "madre"] and familiar._edad >= 18 and
                                totalFactura <= familiar._cuentaBancaria.obtenerSaldo()):
                                familiar._cuentaBancaria.transaccionCuentaAhorros(totalFactura, Funeraria._cuentaAhorros)
                                cliente._listadoFacturas.remove(factura)
                        elif (familiar._parentesco in ["hermano", "hermana"] and familiar._edad >= 18 and
                                totalFactura <= familiar._cuentaBancaria.obtenerSaldo()):
                                familiar._cuentaBancaria.transaccionCuentaAhorros(totalFactura, Funeraria._cuentaAhorros)
                                cliente._listadoFacturas.remove(factura)
                        else:
                            if (totalFactura <= familiar._cuentaBancaria.obtenerSaldo() and
                                familiar._edad >= 18):
                                familiar._cuentaBancaria.transaccionCuentaAhorros(totalFactura, Funeraria._cuentaAhorros)
                                cliente._listadoFacturas.remove(factura)
    
    def cobroFacturas(self, factura):
        tipoServicio = factura._servicio
        totalFactura = factura._total
        resultado = ""
        val = 0
    
        if tipoServicio == "vehiculo":
            if totalFactura <= self._cuentaCorriente._bolsilloTransporte:
                producto = factura._listaProductos[0]
                establecimiento = producto._establecimiento
                self._cuentaCorriente.transaccion(totalFactura, establecimiento._cuentaCorriente, "bolsilloTransporte")
                self._listadoFacturas.insert(0, factura)
                self._listadoFacturasPorPagar.remove(factura)
                val += 1
                resultado = f"Factura con ID: {factura._ID} pagada con éxito"
            else:
                val += 1
                resultado = f"No hay dinero suficiente para pagar la factura con ID: {factura._ID}"
    
        elif tipoServicio == "establecimiento":
            if totalFactura <= self._cuentaCorriente._bolsilloEstablecimientos:
                producto = factura._listaProductos[0]
                establecimiento = producto._establecimiento
                self._cuentaCorriente.transaccion(totalFactura, establecimiento._cuentaCorriente, "bolsilloEstablecimientos")
                self._listadoFacturas.append(factura)
                self._listadoFacturasPorPagar.remove(factura)
                val += 1
                resultado = f"Factura con ID: {factura.getID} pagada con éxito"
            else:
                val += 1
                resultado = f"No hay dinero suficiente para pagar la factura con ID: {factura.getID}"
    
        elif tipoServicio == "empleado":
            if totalFactura <= self._cuentaCorriente._bolsilloTrabajadores:
               producto = factura._listaProductos[0]
               establecimiento = producto._establecimiento
               self._cuentaCorriente.transaccion(totalFactura, establecimiento._cuentaCorriente, "bolsilloTrabajadores")
               self._listadoFacturasPorPagar.remove(factura)
               val += 1
               resultado = f"Factura con ID: {factura.getID} pagada con éxito"
            else:
               val += 1
               resultado = f"No hay dinero suficiente para pagar la factura con ID: {factura.getID}"
    
        elif tipoServicio == "inventario":
            if totalFactura <= self._cuentaCorriente._bolsilloInventario:
                producto = factura._listaProductos[0]
                establecimiento = producto._establecimiento
                self._cuentaCorriente.transaccion(totalFactura, establecimiento._cuentacorriente, "bolsilloInventario")
                self._listadoFacturas.append(factura)
                self._listadoFacturasPorPagar.remove(factura)
                val += 1
                resultado = f"Factura con ID: {factura.getID} pagada con éxito"
            else:
                val += 1
                resultado = f"No hay dinero suficiente para pagar la factura con ID: {factura.getID}"
    
        return resultado

    def informe_gastos_facturas(self):
        bolsilloInventario = 0
        facturasInventario = 0
        bolsilloTransporte = 0
        facturasTransporte = 0
        bolsilloEstablecimientos = 0
        facturasEstablecimientos = 0
        bolsilloPagoCredito = 0
        facturasPagoCredito = 0
        bolsilloTrabajadores = 0
        facturasTrabajadores = 0

        for factura in self._listadoFacturas:
            if factura._servicio == "inventario":
                bolsilloInventario += factura._total
                facturasInventario += 1
            elif factura._servicio == "vehiculo":
                bolsilloTransporte += factura._total
                facturasTransporte += 1
            elif factura._servicio == "establecimiento":
                bolsilloEstablecimientos += factura._total
                facturas_establecimientos += 1
            elif factura._servicio == "empleado":
                bolsilloTrabajadores += factura._total
                facturasTrabajadores += 1
            elif factura._servicio == "credito":
                bolsilloPagoCredito += factura._total
                facturasPagoCredito += 1

        return ("Informe de gastos:\n"
                f"Facturas inventario: {facturasInventario}\n"
                f"Gastos inventario: {bolsilloInventario}\n"
                f"Facturas transporte: {facturasTransporte}\n"
                f"Gastos transporte: {bolsilloTransporte}\n"
                f"Facturas establecimientos: {facturasEstablecimientos}\n"
                f"Gastos establecimientos: {bolsilloEstablecimientos}\n"
                f"Facturas trabajadores: {facturasTrabajadores}\n"
                f"Gastos trabajadores: {bolsilloTrabajadores}\n"
                f"Facturas pago credito: {facturasPagoCredito}\n"
                f"Gastos credito: {bolsilloPagoCredito}")

    def reajuste_dinero(self):
        funerarias = Establecimiento.filtrarEstablecimiento("funeraria")
        inventarioMax = 0
        resultado = ""
        transporteMax = 0
        establecimientoMax = 0
        trabajadoresMax = 0
        creditoMax = 0
        inventario = None
        transporte = None
        establecimiento = None
        trabajadores = None
        credito = None

        for funeraria in funerarias:
            bolsilloInventario = 0
            bolsilloTransporte = 0
            bolsilloEstablecimientos = 0
            bolsilloPagoCredito = 0
            bolsilloTrabajadores = 0

            for factura in funeraria._listadoFacturas:
                if factura._servicio == "inventario":
                    bolsilloInventario += factura._total
                elif factura._servicio == "vehiculo":
                     bolsilloTransporte += factura._total
                elif factura._servicio == "establecimiento":
                    bolsilloEstablecimientos += factura._total
                elif factura._servicio == "empleado":
                    bolsilloTrabajadores += factura._total
                elif factura._servicio == "credito":
                    bolsilloPagoCredito += factura._total

            if bolsilloInventario > inventarioMax:
                #inventario_max = bolsillo_inventario
                inventario = funeraria
            if bolsilloTransporte > transporteMax:
                transporteMax = bolsilloTransporte
                transporte = funeraria
            if bolsilloEstablecimientos > establecimientoMax:
                establecimientoMax = bolsilloEstablecimientos
                establecimiento = funeraria
            if bolsilloTrabajadores > trabajadoresMax:
                trabajadoresMax = bolsilloTrabajadores
                trabajadores = funeraria
            if bolsilloPagoCredito > creditoMax:
                creditoMax = bolsilloPagoCredito
                credito = funeraria

        if inventarioMax == 0:
            resultado += "No hubo Funerarias que necesitaran un reajuste de dinero para inventario\n"
        else:
            Funeraria._cuentaAhorros.transaccion(1000000, inventario._cuentaCorriente, "bolsilloInventario")
            resultado += f"La funeraria: {inventario._nombre} requiere mayor cantidad de dinero para actualizar el inventario, por lo que se le ha transferido 1000000\n"

        if transporteMax == 0:
            resultado += "No hubo Funerarias que necesitaran un reajuste de dinero para transportes\n"
        else:
            Funeraria._cuentaAhorros.transaccion(1000000, transporte._cuentaCorriente, "bolsilloTransporte")
            resultado += f"La funeraria: {transporte._nombre} requiere mayor cantidad de dinero para la compra y la gestion de vehiculos, por lo que se le ha transferido 1000000\n"

        if establecimientoMax == 0:
            resultado += "No hubo Funerarias que necesitaran un reajuste de dinero para establecimientos\n"
        else:
            Funeraria._cuentaAhorros.transaccion(1000000, establecimiento._cuentaCorriente, "bolsilloEstablecimientos")
            resultado += f"La funeraria: {establecimiento._nombre} requiere mayor cantidad de dinero para el pago a los establecimientos, por lo que se le ha transferido 1000000\n"

        if trabajadoresMax == 0:
            resultado += "No hubo Funerarias que necesitaran un reajuste de dinero para trabajadores\n"
        else:
            Funeraria._cuentaAhorros.transaccion(1000000, trabajadores._cuentaCorriente, "bolsilloTrabajadores")
            resultado += f"La funeraria: {trabajadores._nombre} requiere mayor cantidad de dinero para la contratacion y el pago de los empleados, por lo que se le ha transferido 1000000\n"

        if creditoMax == 0:
            resultado += "No hubo Funerarias que necesitaran un reajuste de dinero para credito\n"
        else:
            Funeraria._cuentaAhorros.transaccion(1000000, credito._cuentaCorriente, "bolsilloPagoCredito")
            resultado += f"La funeraria: {credito._nombre} requiere mayor cantidad de dinero para el pago de su credito, por lo que se le ha transferido 1000000"

        return resultado

    def pago_trabajadores(self, empleado):
        trabajos = empleado._trabajosHechos
        calificacion = empleado._calificacion
        paga = empleado._salario

        if 2 <= trabajos <= 5:
            paga *= 1
            if calificacion == 5:
                paga += paga * 0.05
            self._cuentaCorriente.transaccion(paga, empleado._cuentaBancaria, "bolsilloTrabajadores")
            empleado._trabajosHechos = 0
            self._listadoFacturas.append(Factura("FacturaTrabajador", paga, "2024", self, "empleado"))
            return (f"El trabajador ha hecho: {trabajos} trabajos,\n"
                    f"Y tiene una calificacion de: {calificacion}\n"
                    f"por lo que obtuvo una paga de: {paga}")
        elif 5 < trabajos <= 9:
            paga += paga * 0.02
            if calificacion == 5:
                paga += paga * 0.05
            self._cuentaCorriente.transaccion(paga, empleado._cuentaBancaria, "bolsilloTrabajadores")
            empleado._trabajosHechos = 0
            self._listadoFacturas.append(Factura("FacturaTrabajador", paga, "2024", self, "empleado"))
            return (f"El trabajador ha hecho: {trabajos} trabajos,\n"
                    f"Y tiene una calificacion de: {calificacion}\n"
                    f"por lo que obtuvo una paga de: {paga}")
        elif trabajos > 9:
            paga += paga * 0.04
            if calificacion == 5:
                paga += paga * 0.05
            self._cuentaCorriente.transaccion(paga, empleado._cuentaBancaria, "bolsilloTrabajadores")
            empleado._trabajosHechos = 0
            self._listadoFacturas.append(Factura("FacturaTrabajador", paga, "2024", self, "empleado"))
            return (f"El trabajador ha hecho: {trabajos} trabajos,\n"
                    f"Y tiene una calificacion de: {calificacion}\n"
                    f"por lo que obtuvo una paga de: {paga}")
        else:
            return f"El trabajador ha hecho: {trabajos},\npor lo que no obtuvo una paga"

    def pedir_credito(self):
        if len(self._cuentaCorriente_.credito) < 3:
            if len(self._cuentaCorriente._credito) == 0 or (self._cuentaCorriente._credito[-1]._porcentajeCreditoPorPagar <= 0.5):
                establecimientos = Funeraria.buscarPorFuneraria(self, "cementerio")
                establecimientos += Funeraria.buscarPorFuneraria(self, "crematorio")
                oro = 0
                plata = 0
                bronce = 0
                montoCredito = 0

                for establecimiento in reversed(establecimientos):
                    if establecimiento._afiliacion == "oro":
                        oro += 1
                    elif establecimiento._afiliacion == "plata":
                        plata += 1
                    elif establecimiento._afiliacion == "bronce":
                        bronce += 1

                montoCredito += (oro * 50000)
                montoCredito += (plata * 30000)
                montoCredito += (bronce * 10000)

                div = montoCredito / 4
                self._cuentaCorriente.depositar(div, "bolsilloTrabajadores")
                self._cuentaCorriente.depositar(div, "bolsilloTransporte")
                self._cuentaCorriente.depositar(div, "bolsilloInventario")
                self._cuentaCorriente.depositar(div, "bolsilloEstablecimientos")

                montoCredito += (self._cuentaCorriente._interes * montoCredito)
                credito = Factura("credito", montoCredito, "2024", self, "credito")
                self._cuentaCorriente._credito.append(credito)
                return "Credito aceptado"
            else:
                return "Credito rechazado"
        else:
            return "Ya tiene el maximo de creditos activos al tiempo"

    def pagarCredito(self, indiceCredito, porcentaje):
        if 0 <= indiceCredito < len(self._cuentaCorriente._credito):
            credito = self._cuentaCorriente._credito[indiceCredito]
            if credito:
                porcentajeFaltante = credito._porcentajeCreditoPorPagar
                valorFaltante = credito._precio
                if porcentaje <= porcentajeFaltante:
                    pago = self.calcularPago(porcentaje, valorFaltante)
                    if self._cuentaCorriente.bolsilloPagoCredito >= pago:
                        self._cuenta_corriente.retirar(pago, "bolsilloPagoCredito")
                        self.actualizarCredito(credito, porcentajeFaltante, valorFaltante, pago)
                        return "Pago exitoso"
                    else:
                        return "Dinero insuficiente"
                else:
                    return "El porcentaje es mayor a lo que falta por pagar"
            else:
                return "Crédito no encontrado"
        else:
            return f"Índice de crédito inválido {indiceCredito} {porcentaje}"

    def calcularPago(self, porcentaje, valorFaltante):
        return valorFaltante * porcentaje

    def actualizarCredito(self, credito, porcentajeFaltante, valorFaltante, pago):
        nuevoPorcentajeFaltante = porcentajeFaltante - pago / valorFaltante
        nuevoValorFaltante = valorFaltante - pago
        if nuevoPorcentajeFaltante == 0:
            self._cuentaCorriente._credito.remove(credito)
            self._listadoFacturas.append(credito)
        else:
            credito._porcentajeCreditoPorPagar = nuevoPorcentajeFaltante
            credito._precio = nuevoValorFaltante
    
    def asignarVehiculo(self) :
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

    def buscarTipoVehiculo(self, tipoVehiculo):
        for vehiculo in self._vehiculos:
            if vehiculo.isEstado() and vehiculo.getTipoVehiculo() == tipoVehiculo:
                vehiculo.setEstado(False)
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


    def agregarVehiculo(self, vehiculo):
        self._vehiculos.append(vehiculo)

    def agregarEmpleado(self, empleado):
        self._empleados.append(empleado)



    def getClientes(self):
        return self.clientes
    def setClientes(self, clientes):
        self.clientes=clientes

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
    
    def gestionarTransporte(self, cliente, vehiculos, hora: time) -> str: 
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
    