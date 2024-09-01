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
    
  
    
    

    def __init__(self, nombre: str, cuentaCorriente, cuentaAhorros):
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

    def buscarEmpleadosPorHoras(self, horas: time, cargo: str) :
        if 6 <= horas.hour <= 14:
            jornada = "mañana"
        elif 15 <= horas.hour <= 22:
            jornada = "tarde"
        else:
            jornada = "noche"

        return self.buscarEmpleados(jornada, cargo)

  


    def buscarCliente(self, tipoCementerio: str, adultoNino: str) :
        clientes = []
        cementerios = Cementerio.cementerioPorTipo(
            Establecimiento.buscarPorFuneraria(self, "cementerio"), tipoCementerio)

        for cementerio in cementerios:
            cementerio = Cementerio(cementerio)  # Assume Cementerio is a proper class
            clientes.extend(cementerio.buscarCliente(adultoNino))

        return clientes

    def buscarClientePorId(self, idCliente: int) :
        for cliente in self.clientes:
            if cliente.getCC() == idCliente:
                return cliente
        return None
    
    def cobro_servicios_clientes(cliente):
        for i in range(len(cliente.listado_facturas) - 1, -1, -1):
            factura = cliente.listado_facturas[i]
            total_factura = factura.total
            if (cliente.cuenta_bancaria is not None and
                total_factura <= cliente.cuenta_bancaria.obtener_saldo() and
                cliente.edad >= 18):
                cliente.cuenta_bancaria.transaccion_cuenta_ahorros(total_factura, Funeraria.cuenta_ahorros)
                cliente.listado_facturas.remove(factura)
            else:
                for persona in cliente.familiares:
                    if isinstance(persona, Familiar):
                        familiar = persona
                        if familiar.parentesco is not None:
                            if (familiar.parentesco == "conyuge" and familiar.edad >= 18 and
                                total_factura <= familiar.cuenta_bancaria.obtener_saldo()):
                                familiar.cuenta_bancaria.transaccion_cuenta_ahorros(total_factura, Funeraria.cuenta_ahorros)
                                cliente.listado_facturas.remove(factura)
                        elif (familiar.parentesco in ["hijo", "hija"] and familiar.edad >= 18 and
                                total_factura <= familiar.cuenta_bancaria.obtener_saldo()):
                                familiar.cuenta_bancaria.transaccion_cuenta_ahorros(total_factura, Funeraria.cuenta_ahorros)
                                cliente.listado_facturas.remove(factura)
                        elif (familiar.parentesco in ["padre", "madre"] and familiar.edad >= 18 and
                                total_factura <= familiar.cuenta_bancaria.obtener_saldo()):
                                familiar.cuenta_bancaria.transaccion_cuenta_ahorros(total_factura, Funeraria.cuenta_ahorros)
                                cliente.listado_facturas.remove(factura)
                        elif (familiar.parentesco in ["hermano", "hermana"] and familiar.edad >= 18 and
                                total_factura <= familiar.cuenta_bancaria.obtener_saldo()):
                                familiar.cuenta_bancaria.transaccion_cuenta_ahorros(total_factura, Funeraria.cuenta_ahorros)
                                cliente.listado_facturas.remove(factura)
                        else:
                            if (total_factura <= familiar.cuenta_bancaria.obtener_saldo() and
                                familiar.edad >= 18):
                                familiar.cuenta_bancaria.transaccion_cuenta_ahorros(total_factura, Funeraria.cuenta_ahorros)
                                cliente.listado_facturas.remove(factura)
    
    def cobro_facturas(self, factura):
        tipo_servicio = factura.servicio
        total_factura = factura.total
        resultado = ""
        val = 0
    
        if tipo_servicio == "vehiculo":
            if total_factura <= self.cuenta_corriente.bolsillo_transporte:
                producto = factura.lista_productos[0]
                establecimiento = producto.establecimiento
                self.cuenta_corriente.transaccion(total_factura, establecimiento.cuenta_corriente, "bolsillo_transporte")
                self.listado_facturas.insert(0, factura)
                self.listado_facturas_por_pagar.remove(factura)
                val += 1
                resultado = f"Factura con ID: {factura.id} pagada con éxito"
            else:
                val += 1
                resultado = f"No hay dinero suficiente para pagar la factura con ID: {factura.id}"
    
        elif tipo_servicio == "establecimiento":
            if total_factura <= self.cuenta_corriente.bolsillo_establecimientos:
                producto = factura.lista_productos[0]
                establecimiento = producto.establecimiento
                self.cuenta_corriente.transaccion(total_factura, establecimiento.cuenta_corriente, "bolsillo_establecimientos")
                self.listado_facturas.append(factura)
                self.listado_facturas_por_pagar.remove(factura)
                val += 1
                resultado = f"Factura con ID: {factura.id} pagada con éxito"
            else:
                val += 1
                resultado = f"No hay dinero suficiente para pagar la factura con ID: {factura.id}"
    
        elif tipo_servicio == "empleado":
            if total_factura <= self.cuenta_corriente.bolsillo_trabajadores:
               producto = factura.lista_productos[0]
               establecimiento = producto.establecimiento
               self.cuenta_corriente.transaccion(total_factura, establecimiento.cuenta_corriente, "bolsillo_trabajadores")
               self.listado_facturas_por_pagar.remove(factura)
               val += 1
               resultado = f"Factura con ID: {factura.id} pagada con éxito"
            else:
               val += 1
               resultado = f"No hay dinero suficiente para pagar la factura con ID: {factura.id}"
    
        elif tipo_servicio == "inventario":
            if total_factura <= self.cuenta_corriente.bolsillo_inventario:
                producto = factura.lista_productos[0]
                establecimiento = producto.establecimiento
                self.cuenta_corriente.transaccion(total_factura, establecimiento.cuenta_corriente, "bolsillo_inventario")
                self.listado_facturas.append(factura)
                self.listado_facturas_por_pagar.remove(factura)
                val += 1
                resultado = f"Factura con ID: {factura.id} pagada con éxito"
            else:
                val += 1
                resultado = f"No hay dinero suficiente para pagar la factura con ID: {factura.id}"
    
        return resultado

    def informe_gastos_facturas(self):
        bolsillo_inventario = 0
        facturas_inventario = 0
        bolsillo_transporte = 0
        facturas_transporte = 0
        bolsillo_establecimientos = 0
        facturas_establecimientos = 0
        bolsillo_pago_credito = 0
        facturas_pago_credito = 0
        bolsillo_trabajadores = 0
        facturas_trabajadores = 0

        for factura in self.listado_facturas:
            if factura.servicio == "inventario":
                bolsillo_inventario += factura.total
                facturas_inventario += 1
            elif factura.servicio == "vehiculo":
                bolsillo_transporte += factura.total
                facturas_transporte += 1
            elif factura.servicio == "establecimiento":
                bolsillo_establecimientos += factura.total
                facturas_establecimientos += 1
            elif factura.servicio == "empleado":
                bolsillo_trabajadores += factura.total
                facturas_trabajadores += 1
            elif factura.servicio == "credito":
                bolsillo_pago_credito += factura.total
                facturas_pago_credito += 1

        return ("Informe de gastos:\n"
                f"Facturas inventario: {facturas_inventario}\n"
                f"Gastos inventario: {bolsillo_inventario}\n"
                f"Facturas transporte: {facturas_transporte}\n"
                f"Gastos transporte: {bolsillo_transporte}\n"
                f"Facturas establecimientos: {facturas_establecimientos}\n"
                f"Gastos establecimientos: {bolsillo_establecimientos}\n"
                f"Facturas trabajadores: {facturas_trabajadores}\n"
                f"Gastos trabajadores: {bolsillo_trabajadores}\n"
                f"Facturas pago credito: {facturas_pago_credito}\n"
                f"Gastos credito: {bolsillo_pago_credito}")

    def reajuste_dinero(self):
        funerarias = Establecimiento.filtrar_establecimiento("funeraria")
        inventario_max = 0
        resultado = ""
        transporte_max = 0
        establecimiento_max = 0
        trabajadores_max = 0
        credito_max = 0
        inventario = None
        transporte = None
        establecimiento = None
        trabajadores = None
        credito = None

        for funeraria in funerarias:
            bolsillo_inventario = 0
            bolsillo_transporte = 0
            bolsillo_establecimientos = 0
            bolsillo_pago_credito = 0
            bolsillo_trabajadores = 0

            for factura in funeraria.listado_facturas:
                if factura.servicio == "inventario":
                    bolsillo_inventario += factura.total
                elif factura.servicio == "vehiculo":
                     bolsillo_transporte += factura.total
                elif factura.servicio == "establecimiento":
                    bolsillo_establecimientos += factura.total
                elif factura.servicio == "empleado":
                    bolsillo_trabajadores += factura.total
                elif factura.servicio == "credito":
                    bolsillo_pago_credito += factura.total

            if bolsillo_inventario > inventario_max:
                inventario_max = bolsillo_inventario
                inventario = funeraria
            if bolsillo_transporte > transporte_max:
                transporte_max = bolsillo_transporte
                transporte = funeraria
            if bolsillo_establecimientos > establecimiento_max:
                establecimiento_max = bolsillo_establecimientos
                establecimiento = funeraria
            if bolsillo_trabajadores > trabajadores_max:
                trabajadores_max = bolsillo_trabajadores
                trabajadores = funeraria
            if bolsillo_pago_credito > credito_max:
                credito_max = bolsillo_pago_credito
                credito = funeraria

        if inventario_max == 0:
            resultado += "No hubo Funerarias que necesitaran un reajuste de dinero para inventario\n"
        else:
            Funeraria._cuentaAhorros.transaccion(1000000, inventario.cuenta_corriente, "bolsilloInventario")
            resultado += f"La funeraria: {inventario.nombre} requiere mayor cantidad de dinero para actualizar el inventario, por lo que se le ha transferido 1000000\n"

        if transporte_max == 0:
            resultado += "No hubo Funerarias que necesitaran un reajuste de dinero para transportes\n"
        else:
            Funeraria._cuentaAhorros.transaccion(1000000, transporte.cuenta_corriente, "bolsilloTransporte")
            resultado += f"La funeraria: {transporte.nombre} requiere mayor cantidad de dinero para la compra y la gestion de vehiculos, por lo que se le ha transferido 1000000\n"

        if establecimiento_max == 0:
            resultado += "No hubo Funerarias que necesitaran un reajuste de dinero para establecimientos\n"
        else:
            Funeraria._cuentaAhorros.transaccion(1000000, establecimiento.cuenta_corriente, "bolsilloEstablecimientos")
            resultado += f"La funeraria: {establecimiento.nombre} requiere mayor cantidad de dinero para el pago a los establecimientos, por lo que se le ha transferido 1000000\n"

        if trabajadores_max == 0:
            resultado += "No hubo Funerarias que necesitaran un reajuste de dinero para trabajadores\n"
        else:
            Funeraria._cuentaAhorros.transaccion(1000000, trabajadores.cuenta_corriente, "bolsilloTrabajadores")
            resultado += f"La funeraria: {trabajadores.nombre} requiere mayor cantidad de dinero para la contratacion y el pago de los empleados, por lo que se le ha transferido 1000000\n"

        if credito_max == 0:
            resultado += "No hubo Funerarias que necesitaran un reajuste de dinero para credito\n"
        else:
            Funeraria._cuentaAhorros.transaccion(1000000, credito.cuenta_corriente, "bolsilloPagoCredito")
            resultado += f"La funeraria: {credito.nombre} requiere mayor cantidad de dinero para el pago de su credito, por lo que se le ha transferido 1000000"

        return resultado

    def pago_trabajadores(self, empleado):
        trabajos = empleado.trabajos_hechos
        calificacion = empleado.calificacion
        paga = empleado.salario

        if 2 <= trabajos <= 5:
            paga *= 1
            if calificacion == 5:
                paga += paga * 0.05
            self.cuenta_corriente.transaccion(paga, empleado.cuenta_bancaria, "bolsilloTrabajadores")
            empleado.trabajos_hechos = 0
            self.listado_facturas.append(Factura("FacturaTrabajador", paga, "2024", self, "empleado"))
            return (f"El trabajador ha hecho: {trabajos} trabajos,\n"
                    f"Y tiene una calificacion de: {calificacion}\n"
                    f"por lo que obtuvo una paga de: {paga}")
        elif 5 < trabajos <= 9:
            paga += paga * 0.02
            if calificacion == 5:
                paga += paga * 0.05
            self.cuenta_corriente.transaccion(paga, empleado.cuenta_bancaria, "bolsilloTrabajadores")
            empleado.trabajos_hechos = 0
            self.listado_facturas.append(Factura("FacturaTrabajador", paga, "2024", self, "empleado"))
            return (f"El trabajador ha hecho: {trabajos} trabajos,\n"
                    f"Y tiene una calificacion de: {calificacion}\n"
                    f"por lo que obtuvo una paga de: {paga}")
        elif trabajos > 9:
            paga += paga * 0.04
            if calificacion == 5:
                paga += paga * 0.05
            self.cuenta_corriente.transaccion(paga, empleado.cuenta_bancaria, "bolsilloTrabajadores")
            empleado.trabajos_hechos = 0
            self.listado_facturas.append(Factura("FacturaTrabajador", paga, "2024", self, "empleado"))
            return (f"El trabajador ha hecho: {trabajos} trabajos,\n"
                    f"Y tiene una calificacion de: {calificacion}\n"
                    f"por lo que obtuvo una paga de: {paga}")
        else:
            return f"El trabajador ha hecho: {trabajos},\npor lo que no obtuvo una paga"

    def pedir_credito(self):
        if len(self.cuenta_corriente.credito) < 3:
            if len(self.cuenta_corriente.credito) == 0 or (self.cuenta_corriente.credito[-1].porcentaje_credito_por_pagar <= 0.5):
                establecimientos = Funeraria.buscar_por_funeraria(self, "cementerio")
                establecimientos += Funeraria.buscar_por_funeraria(self, "crematorio")
                oro = 0
                plata = 0
                bronce = 0
                monto_credito = 0

                for establecimiento in reversed(establecimientos):
                    if establecimiento.afiliacion == "oro":
                        oro += 1
                    elif establecimiento.afiliacion == "plata":
                        plata += 1
                    elif establecimiento.afiliacion == "bronce":
                        bronce += 1

                monto_credito += (oro * 50000)
                monto_credito += (plata * 30000)
                monto_credito += (bronce * 10000)

                div = monto_credito / 4
                self.cuenta_corriente.depositar(div, "bolsilloTrabajadores")
                self.cuenta_corriente.depositar(div, "bolsilloTransporte")
                self.cuenta_corriente.depositar(div, "bolsilloInventario")
                self.cuenta_corriente.depositar(div, "bolsilloEstablecimientos")

                monto_credito += (self.cuenta_corriente.interes * monto_credito)
                credito = Factura("credito", monto_credito, "2024", self, "credito")
                self.cuenta_corriente.credito.append(credito)
                return "Credito aceptado"
            else:
                return "Credito rechazado"
        else:
            return "Ya tiene el maximo de creditos activos al tiempo"

    def pagar_credito(self, indice_credito, porcentaje):
        if 0 <= indice_credito < len(self.cuenta_corriente.credito):
            credito = self.cuenta_corriente.credito[indice_credito]
            if credito:
                porcentaje_faltante = credito.porcentaje_credito_por_pagar
                valor_faltante = credito.precio
                if porcentaje <= porcentaje_faltante:
                    pago = self.calcular_pago(porcentaje, valor_faltante)
                    if self.cuenta_corriente.bolsillo_pago_credito >= pago:
                        self.cuenta_corriente.retirar(pago, "bolsilloPagoCredito")
                        self.actualizar_credito(credito, porcentaje_faltante, valor_faltante, pago)
                        return "Pago exitoso"
                    else:
                        return "Dinero insuficiente"
                else:
                    return "El porcentaje es mayor a lo que falta por pagar"
            else:
                return "Crédito no encontrado"
        else:
            return f"Índice de crédito inválido {indice_credito} {porcentaje}"

    def calcular_pago(self, porcentaje, valor_faltante):
        return valor_faltante * porcentaje

    def actualizar_credito(self, credito, porcentaje_faltante, valor_faltante, pago):
        nuevo_porcentaje_faltante = porcentaje_faltante - pago / valor_faltante
        nuevo_valor_faltante = valor_faltante - pago
        if nuevo_porcentaje_faltante == 0:
            self.cuenta_corriente.credito.remove(credito)
            self.listado_facturas.append(credito)
        else:
            credito.porcentaje_credito_por_pagar = nuevo_porcentaje_faltante
            credito.precio = nuevo_valor_faltante
    
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
    