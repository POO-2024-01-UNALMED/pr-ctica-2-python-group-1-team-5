from gestorAplicacion.financiero.banco import Banco
from gestorAplicacion.financiero.cuentaBancaria import CuentaBancaria
from gestorAplicacion.financiero.factura import Factura
from gestorAplicacion.inventario.vehiculo import Vehiculo
from gestorAplicacion.establecimientos.establecimiento import Establecimiento
#from gestorAplicacion.establecimientos.cementerio import Cementerio
#from gestorAplicacion.establecimientos.crematorio import Crematorio
from gestorAplicacion.establecimientos.funeraria import Funeraria
from gestorAplicacion.personas.persona import Persona
from gestorAplicacion.personas.cliente import Cliente
from gestorAplicacion.personas.empleado import Empleado
from gestorAplicacion.personas.familiar import Familiar
from gestorAplicacion.inventario.urna import Urna
from gestorAplicacion.inventario.tumba import Tumba
from gestorAplicacion.inventario.producto import Producto

def funcionalidadGestionInventario(funerarias):
    # Paso 1: Seleccionar y mostrar información de la funeraria
    funeraria_seleccionada = seleccionarFuneraria(funerarias)
    imprimirInformacion(funeraria_seleccionada)

    # Paso 2: Realizar intercambio entre funerarias si es posible
    if analizarIntercambios(funerarias, funeraria_seleccionada):
        # Si el intercambio es posible, procede con la asignación de recursos
        asignarRecursos(funeraria_seleccionada)

    # Paso 3: Comprar productos faltantes o contratar empleados
    realizarCompras(funeraria_seleccionada)

    # Paso 4: Realizar encuesta
    realizarEncuesta(funeraria_seleccionada)

    print("Proceso completado.")


def seleccionarFuneraria(funerarias):
    # Bucle infinito que mantiene la solicitud de selección de funeraria hasta que se realice una elección válida
    while True:
        print("Seleccione una funeraria:")
        # Recorre la lista de funerarias para mostrarlas con un número correspondiente
        for i, funeraria in enumerate(funerarias):
            print(f"{i + 1}. {funeraria.getNombre()}")
            print("   ____")
            print("  /    \\")
            print(" /______\\")
            print(f" |      |  {funeraria.getNombre()}")
            print(" |______|")
            print()
        print(f"{len(funerarias) + 1}. Cancelar")

        seleccion = int(input()) - 1
        # Verifica si la selección está dentro del rango válido de funerarias
        if 0 <= seleccion < len(funerarias):
            # Devuelve la funeraria seleccionada
            return funerarias[seleccion]
        elif seleccion == len(funerarias):
            # Si la selección es la opción de cancelar, imprime un mensaje y termina el programa
            print("Proceso cancelado.")
            exit(0)
        else:
            print("Selección inválida. Intente de nuevo.")


def imprimirInformacion(funeraria):
    print(f"Nombre: {funeraria.getNombre()}")
    print(f"Calificación: {funeraria.getCalificacion()}")
    print(f"Cantidad de empleados: {len(funeraria.getEmpleados())}")

    # Calcula los productos vendidos en la funeraria
    productos_vendidos = funeraria.calcularProductosVendidos()

    print("Productos más vendidos:")

    # Variable para rastrear el producto más vendido y la cantidad máxima vendida
    masVendido = None
    maxVendidas = 0

    # Recorre la lista de productos vendidos
    for producto in productos_vendidos:
        # Imprime el nombre del producto y la cantidad vendida
        print(f"- {producto.getNombre()}: {producto.getCantidadVendida()} vendidas")

        # Si la cantidad vendida de este producto es mayor que la máxima registrada, actualiza las variables correspondientes
        if producto.cantidad_vendida > maxVendidas:
            masVendido = producto
            maxVendidas = producto.getCantidadVendida()

    # Si hay un producto más vendido, lo imprime
    if masVendido:
        print(f"El producto más vendido es {masVendido.getNombre()} con {masVendido.cantidadVendida()} unidades vendidas.")

    print("------------------------")

def analizarIntercambios(funerarias, funeraria_seleccionada):
    while True:  # Bucle para asegurar que el usuario proporcione una respuesta válida
        # Solicita al usuario si desea realizar un intercambio de productos entre funerarias
        respuesta = input("¿Desea realizar un intercambio de productos entre funerarias? (si/no): ").strip().lower()

        if respuesta == "si":
            funeraria_con_mayor_stock = None
            producto_con_mayor_stock = None
            
            # Encuentra la funeraria con mayor stock de productos
            for f in funerarias:
                if f != funeraria_seleccionada:  # evita la funeraria seleccionada
                    for p in f.productos:
                        # Verifica si este producto tiene mayor stock que el actual producto con mayor stock registrado
                        if producto_con_mayor_stock is None or p.cantidad > producto_con_mayor_stock.cantidad:
                            producto_con_mayor_stock = p
                            funeraria_con_mayor_stock = f
            
            # Verifica si se encontró una funeraria y un producto con mayor stock para el intercambio
            if funeraria_con_mayor_stock and producto_con_mayor_stock:
                producto_intercambiado = producto_con_mayor_stock

                funeraria_con_mayor_stock.getProductos().remove(producto_intercambiado)
                funeraria_seleccionada.getProductos().append(producto_intercambiado)

                print("Se ha realizado un intercambio:")
                print(f"Producto intercambiado: {producto_intercambiado.getNombre()}")
                print(f"De la funeraria: {funeraria_con_mayor_stock.getNombre()}")
                print(f"A la funeraria: {funeraria_seleccionada.getNombre()}")

                return True  # Intercambio realizado
            else:
                print("No se encontraron productos para intercambiar.")
                return False  # No se realizó el intercambio

        elif respuesta == "no":
            print("No se realizará ningún intercambio.")
            return False

        else:
            print("Respuesta no válida. Por favor, responda 'si' o 'no'.")


def realizarIntercambio(funeraria_a, funeraria_b, producto_a, producto_b):
    # Seleccionar empleados
    print("Seleccione hasta dos empleados para realizar el intercambio:")
    empleados_seleccionados = seleccionarEmpleados(funeraria_a)

    # Seleccionar un vehículo
    print("Seleccione un vehículo para realizar el intercambio:")
    vehiculos_seleccionados = seleccionarVehiculos(funeraria_a)

    # Mostrar productos y realizar intercambio
    print(f"Seleccione la cantidad de {producto_a.nombre} para intercambiar:")
    cantidad_intercambio = seleccionarCantidadProducto(producto_a)

    realizarIntercambioProductos(funeraria_a, funeraria_b, producto_a, producto_b, cantidad_intercambio, empleados_seleccionados, vehiculos_seleccionados)


def seleccionarEmpleados(funeraria):
    empleados_seleccionados = []
    max_empleados = 1  # Número máximo de empleados a seleccionar

    for empleado in funeraria.getEmpleados():
        print(f"{empleado.getNombre()} ({empleado.getCargo()}) - Jornada: {empleado.getJornada()}")
        print("    O ")
        print("   /|\\")
        print("   / \\")
        respuesta = input("¿Seleccionar este empleado? (S/N): ")

        if respuesta.strip().lower() == "s":
            if len(empleados_seleccionados) < max_empleados:
                empleados_seleccionados.append(empleado)
            else:
                print("Ya ha seleccionado el máximo de empleados permitidos.")
                break

    while len(empleados_seleccionados) < max_empleados:
        print(f"Debe seleccionar exactamente {max_empleados} empleados. Seleccione más empleados:")
        for empleado in funeraria.getEmpleados():
            if empleado not in empleados_seleccionados:
                print(f"{empleado.getNombre()} ({empleado.getCargo()}) - Jornada: {empleado.getJornada()}")
                print("    O ")
                print("   /|\\")
                print("   / \\")
                respuesta = input("¿Seleccionar este empleado? (S/N): ")

                if respuesta.strip().lower() == "s":
                    empleados_seleccionados.append(empleado)
                    if len(empleados_seleccionados) >= max_empleados:
                        break

    return empleados_seleccionados

def seleccionarVehiculos(funeraria):
    vehiculos_seleccionados = []
    max_vehiculos = 1  # Define el número máximo de vehículos que se pueden seleccionar

    # Itera sobre la lista de vehículos de la funeraria e imprime la información
    for vehiculo in funeraria.getVehiculos():
        print(f"{vehiculo.getTipoVehiculo()} - Capacidad: {vehiculo.getCapacidad()}")

        # Verifica si tiene un conductor asignado
        if vehiculo.conductor is not None:
            print(f"Conductor: {vehiculo.geConductorNombre()}")

        # Dibujo del vehículo
        print("   ______")
        print("  /|_||_\\.__")
        print(" (   _    _ _\\")
        print(" =-(_)--(_)-'")
        respuesta = input("¿Seleccionar este vehículo? (S/N): ").strip().lower()

        if respuesta == 's':
            if len(vehiculos_seleccionados) < max_vehiculos:
                vehiculos_seleccionados.append(vehiculo)
            else:
                print("Ya ha seleccionado el máximo de vehículos permitidos.")
                break

    return vehiculos_seleccionados


def seleccionarCantidadProducto(producto):
    cantidad = int(input(f"Ingrese la cantidad de {producto.getNombre()} para intercambiar: "))
    return cantidad


def realizarIntercambioProductos(funeraria_a, funeraria_b, producto_a, producto_b, cantidad, empleados, vehiculos):
    # Paso 1: Seleccionar productos a intercambiar
    print("Seleccione los productos que desea intercambiar:")
    productos_a_seleccionados = []

    for producto in funeraria_a.productos:
        if producto.cantidad > 0:  # Solo permite seleccionar productos con cantidad disponible
            print(f"Producto: {producto.getNombre()}, Cantidad disponible: {producto.getCantidad()}")
            respuesta = input("¿Desea intercambiar este producto? (S/N): ").strip().lower()

            if respuesta == 's':
                cantidad_a_intercambiar = int(input("Ingrese la cantidad a intercambiar: "))

                if 0 < cantidad_a_intercambiar <= producto.getCantidad():
                    producto_seleccionado = Producto(producto.getNombre(), producto.getPrecio(), cantidad_a_intercambiar)
                    productos_a_seleccionados.append(producto_seleccionado)
                    producto.getCantidad() -= cantidad_a_intercambiar
                else:
                    print("Cantidad inválida. El intercambio no se realizará.")
    
    # Paso 2: Seleccionar empleados
    print("Seleccione hasta dos empleados para realizar el intercambio:")
    empleados_seleccionados = seleccionarEmpleados(funeraria_a)

    # Paso 3: Seleccionar vehículos
    print("Seleccione un vehículo para realizar el intercambio:")
    vehiculos_seleccionados = seleccionarVehiculos(funeraria_a)

    # Paso 4: Mostrar resumen del intercambio
    print("Resumen del intercambio:")
    print(f"Productos de {funeraria_a.getNombre()} a intercambiar:")
    for producto in productos_a_seleccionados:
        print(f"- {producto.getNombre()}: {producto.getCantidad()} unidades")

    print("Empleados seleccionados:")
    for empleado in empleados_seleccionados:
        print(f"- {empleado.getNombre()} ({empleado.getCargo()})")

    print("Vehículos seleccionados:")
    for vehiculo in vehiculos_seleccionados:
        print(f"- {vehiculo.getTipoVhiculo()}")
        if vehiculo.getConductor():
            print(f"  Conductor: {vehiculo.getConductor().getNombre()}")
        else:
            print("  Conductor: No asignado")

    # Confirmar el intercambio
    confirmacion = input("¿Desea confirmar el intercambio? (S/N): ").strip().lower()
    if confirmacion == 's':
        # Realizar el intercambio de productos
        for producto in productos_a_seleccionados:
            funeraria_b.agregarProducto(producto)

        # Asignar los empleados y vehículos a las funerarias correspondientes
        for empleado in empleados_seleccionados:
            funeraria_a.agregarEmpleado(empleado)

        for vehiculo in vehiculos_seleccionados:
            funeraria_a.agregarVehiculo(vehiculo)

        print("Intercambio realizado exitosamente.")
    else:
        print("Intercambio cancelado.")

def realizarCompras(funeraria):
    # Identifica los productos con menos de 10 existencias en la funeraria
    productos_faltantes = funeraria.identificarProductosFaltantes()

    # Verifica si hay productos faltantes
    if len(productos_faltantes) > 0:
        print("Productos con menos de 10 existencias:")
        for producto in productos_faltantes:
            print(f"- {producto.getNombre()}: {producto.getCantidad()}")

        # Opciones: comprar productos, contratar empleados, o comprar vehículos
        print("Seleccione una opción:")
        print("1. Comprar productos")
        print("2. Contratar empleados")
        print("3. Comprar vehículos")
        print("4. Cancelar")

        opcion = int(input())
        
        # Ejecuta la acción correspondiente a la opción seleccionada
        if opcion == 1:
            comprarProductos(funeraria, productos_faltantes)
        elif opcion == 2:
            contratarEmpleados(funeraria)
        elif opcion == 3:
            comprarVehiculos(funeraria)
        elif opcion == 4:
            print("Operación cancelada.")
            return
        else:
            print("Opción inválida.")
            realizarCompras(funeraria)
    else:
        print("No hay productos faltantes.")


def comprarProductos(funeraria, productos_faltantes):
    # Muestra una lista de establecimientos que pueden vender los productos faltantes
    print("Establecimientos que pueden vender los productos faltantes:")

    # Itera sobre la lista de proveedores de la funeraria
    for i, est in enumerate(funeraria.getListadoProveedores()):
        print(f"{i + 1}. {est.getNombre()} (Calificación: {est.getCalificacion()})")

    # Seleccionar establecimiento
    seleccion_establecimiento = int(input("Seleccione el establecimiento para realizar la compra: ")) - 1

    if 0 <= seleccion_establecimiento < len(funeraria.getListadoProveedores()):
        proveedor_seleccionado = funeraria.getlistadoProveedores()[seleccion_establecimiento]
        productos_comprados = []

        # Mostrar productos faltantes y realizar la compra
        for producto_faltante in productos_faltantes:
            if proveedor_seleccionado.tieneProducto(producto_faltante.getNombre()):
                respuesta = input(f"¿Desea comprar {producto_faltante.getNombre()}? (S/N): ").strip().lower()

                if respuesta == 's':
                    cantidad_compra = int(input("Ingrese la cantidad a comprar: "))

                    if cantidad_compra > 0:
                        # Actualizar inventario
                        producto_faltante.getCantidad() += cantidad_compra
                        productos_comprados.append(Producto(producto_faltante.getNombre(), cantidad_compra))
                        print("Compra realizada exitosamente.")
                    else:
                        print("Cantidad inválida. La compra no se realizará.")
        
        # Mostrar resumen de la compra
        if productos_comprados:
            print("Resumen de la compra de productos:")
            for producto in productos_comprados:
                print(f"  Producto: {producto.getNombre()}, Cantidad comprada: {producto.getCantidad()}")
        else:
            print("No se realizaron compras.")
    else:
        print("Selección de establecimiento inválida.")

def contratarEmpleados(funeraria):
    print("Establecimientos disponibles para contratación de empleados:")

    establecimientos = funeraria.getListadoProveedoresEmpleados()
    for i, establecimiento in enumerate(establecimientos):
        print(f"{i + 1}. {establecimiento.getNombre()} (Calificación: {establecimiento.getCalificacion()})")

    # Seleccionar establecimiento
    print("Seleccione el establecimiento para ver sus empleados:")
    seleccionEstablecimiento = int(input()) - 1

    if 0 <= seleccionEstablecimiento < len(establecimientos):
        estSeleccionado = establecimientos[seleccionEstablecimiento]
        empleadosContratados = []

        # Mostrar empleados disponibles para contratación
        print(f"Empleados disponibles en {estSeleccionado.getNombre()}:")
        for empleado in estSeleccionado.getEmpleados():
            print(f"  Empleado: {empleado.getNombre()}, Cargo: {empleado.getCargo()}, Experiencia: {empleado.getExperiencia()} años, Edad: {empleado.getEdad()}")
            print("¿Desea contratar este empleado? (S/N)")
            respuesta = input().strip().lower()
            if respuesta == 's':
                funeraria.agregarEmpleado(empleado)
                empleadosContratados.append(empleado)
                print(f"Empleado {empleado.getNombre()} contratado exitosamente.")

        # Mostrar resumen de la contratación
        if empleadosContratados:
            print("Resumen de la contratación de empleados:")
            for empleado in empleadosContratados:
                print(f"  Empleado: {empleado.getNombre()}, Cargo: {empleado.getCargo()}, Experiencia: {empleado.getExperiencia()} años, Edad: {empleado.getEdad()}")
        else:
            print("No se contrataron empleados.")
    else:
        print("Selección inválida.")

def comprarVehiculos(funeraria):
    print("Establecimientos disponibles para compra de vehículos:")

    establecimientos = funeraria.listadoProveedoresVehiculos()
    for i, est in enumerate(establecimientos):
        print(f"{i + 1}. {est.getNombre()} (Calificación: {est.getCalificacion()})")

    # Seleccionar establecimiento
    seleccion_establecimiento = int(input("Seleccione el establecimiento para ver sus vehículos: ")) - 1

    if 0 <= seleccion_establecimiento < len(establecimientos):
        est_seleccionado = establecimientos[seleccion_establecimiento]
        vehiculos_comprados = []

        # Mostrar vehículos disponibles para compra
        print(f"Vehículos disponibles en {est_seleccionado.getNombre()}:")
        for vehiculo in est_seleccionado.vehiculosEnVenta():
            print(f"  Vehículo: {vehiculo.tipoVehiculo()}, Capacidad: {vehiculo.getCapacidad()}, Precio: {vehiculo.getPrecio()}")
            respuesta = input("¿Desea comprar este vehículo? (S/N): ").strip().lower()

            if respuesta == 's':
                funeraria.agregarVehiculo(vehiculo)
                est_seleccionado.removerVehiculoEnVenta(vehiculo)
                vehiculos_comprados.append(vehiculo)
                print("Vehículo comprado exitosamente.")

        # Mostrar resumen de la compra
        if vehiculos_comprados:
            print("Resumen de la compra de vehículos:")
            for vehiculo in vehiculos_comprados:
                print(f"  Vehículo: {vehiculo.getTipoVehiculo()}, Precio: {vehiculo.getPrecio()}")
        else:
            print("No se realizaron compras.")
    else:
        print("Selección inválida.")

def realizarEncuesta(funeraria):
    print("Realizando encuesta de desempeño...")

    # Encuesta para el proceso en general
    calificacion = int(input("Califique el desempeño del proceso en general (1-5): "))
    descripcion = input("Ingrese una descripción opcional sobre el desempeño del proceso: ")

    # Guardar la calificación y descripción en la funeraria
    funeraria.getCalificacion() = calificacion
    funeraria.getDescripcionCalificacion() = descripcion

    print(f"Calificación del proceso guardada: {calificacion}")
    if descripcion:
        print(f"Descripción: {descripcion}")

    print("Encuesta completada. Gracias por su retroalimentación.")


def asignarRecursos(funeraria):
    print(f"Asignación de recursos para la funeraria: {funeraria.getNombre()}")

    # Selección de empleados
    print("Seleccione los empleados para realizar la tarea:")
    empleados_seleccionados = seleccionarEmpleados(funeraria)

    # Selección de vehículos
    print("Seleccione los vehículos para realizar la tarea:")
    vehiculos_seleccionados = seleccionarVehiculos(funeraria)

    # Selección de productos
    print("Seleccione los productos a enviar:")
    productos_seleccionados = []
    for producto in funeraria.productos:
        print(f"{producto.getNombre()} - Cantidad disponible: {producto.getCantidad()}")
        cantidad = int(input("¿Cuántos desea enviar? "))
        if 0 < cantidad <= producto.getCantidad():
            producto_seleccionado = Producto(producto.getNombre(), producto.getPrecio(), cantidad)
            productos_seleccionados.append(producto_seleccionado)

    # Mostrar resumen de recursos seleccionados
    print("Resumen de recursos asignados:")
    print("Empleados:")
    for empleado in empleados_seleccionados:
        print(f"- {empleado.getNombre()} ({empleado.getCargo()})")

    print("Vehículos:")
    for vehiculo in vehiculos_seleccionados:
        print(f"- {vehiculo.getTipoVehiculo()}")
        if vehiculo.getConductor():
            print(f"  Conductor: {vehiculo.getConductor().getNombre()}")
        else:
            print("  Conductor: No asignado")

    print("Productos:")
    for producto in productos_seleccionados:
        print(f"- {producto.getNombre()}: {producto.getCantidad()} unidades")