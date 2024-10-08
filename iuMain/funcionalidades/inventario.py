from tkinter import messagebox
from gestorAplicacion.financiero.banco import Banco
from gestorAplicacion.financiero.cuentaBancaria import CuentaBancaria
from gestorAplicacion.financiero.factura import Factura
from gestorAplicacion.inventario.vehiculo import Vehiculo
from gestorAplicacion.establecimientos.establecimiento import Establecimiento
from gestorAplicacion.establecimientos.cementerio import Cementerio
from gestorAplicacion.establecimientos.crematorio import Crematorio
from gestorAplicacion.establecimientos.funeraria import Funeraria
from gestorAplicacion.personas.persona import Persona
from gestorAplicacion.personas.cliente import Cliente
from gestorAplicacion.personas.empleado import Empleado
from gestorAplicacion.personas.familiar import Familiar
from gestorAplicacion.inventario.urna import Urna
from gestorAplicacion.inventario.tumba import Tumba
from gestorAplicacion.inventario.producto import Producto

import tkinter as tk
from tkinter import ttk
from tkinter import Frame, Label, Button
from iuMain.manejoErrores.errorAplicacion import ErrorAplicacion
from iuMain.manejoErrores.errorAplicacion import errorNumeros
from iuMain.manejoErrores.errorAplicacion import CalificacionIncompleta
from iuMain.manejoErrores.errorAplicacion import DescripcionIncompleta 
from iuMain.manejoErrores.errorAplicacion import CamposIncompletos
from iuMain.frame import frame1
from iuMain.frame import tablas
from iuMain.frame import FieldFrame



selected_funeraria = None

def funcionalidadGestionInventario(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    seleccionar_funeraria(frame)

def seleccionar_funeraria(frame):
    frame1 = Frame(frame, bg= "white")
    frame1.pack(fill = "both", expand = True)
    funerarias= Establecimiento.filtrarEstablecimiento("funeraria")

    # Crear etiquetas y opciones para el frame1
    etiqueta = tk.Label(frame1, text="Seleccione una funeraria:", bg="white")
    etiqueta.pack(pady=10)
    opciones = funerarias
    seleccion_var = tk.StringVar(value=opciones[0])

    # Crear un menú desplegable dentro de frame1
    dropdown = tk.OptionMenu(frame1, seleccion_var, *opciones)
    dropdown.pack(pady=10)

    mensaje_label = tk.Label(frame1, text="", bg="white")
    mensaje_label.pack(pady=10)
    def obtener_funeraria_por_nombre(nombre):
        for funeraria in funerarias:
            if funeraria.getNombre() == nombre:
                return funeraria
    

    def continuar_seleccion():
        selected_funeraria_nombre  = seleccion_var.get()
        selected_funeraria = obtener_funeraria_por_nombre(selected_funeraria_nombre)
        if selected_funeraria:
            mensaje_label.config(text=f"Funeraria seleccionada: {selected_funeraria.getNombre()}")
            analisisMercadeo(selected_funeraria, frame)
        else:
            None # poner excepcion

    continuar_button = tk.Button(frame, text="Continuar", command=continuar_seleccion)
    continuar_button.pack(pady=10)

def analisisMercadeo(funeraria, master_frame):
    # Limpiar el frame anterior
    for widget in master_frame.winfo_children():
        widget.destroy()

    productos_vendidos = funeraria.calcularProductosVendidos()
    productos_vendidos = [p for p in productos_vendidos if isinstance(p, Producto)]  # Filtrar solo productos

    # Validar que los productos tengan una cantidad vendida válida
    productos_vendidos = [p for p in productos_vendidos if isinstance(p.getCantidadVendida(), (int, float))]

    # Preparar los datos para mostrar
    productos_mas_vendidos = sorted(productos_vendidos, key=lambda p: p.getCantidadVendida(), reverse=True)
    
    if not productos_vendidos:
        tk.messagebox.showinfo("Información", "No hay productos vendidos para analizar.")
        return

    # Ordenar los productos por la cantidad vendida
    
    
    # Crear un nuevo frame para mostrar la información
    analisis_frame = Frame(master_frame)
    analisis_frame.pack(padx=10, pady=10, fill='both', expand=True)
    
    # Etiquetas para encabezados
    encabezado_frame = Frame(analisis_frame)
    encabezado_frame.pack(fill='x', pady=5)
    
    Label(encabezado_frame, text="Producto", borderwidth=2, relief="solid", width=20).pack(side='left', padx=2)
    Label(encabezado_frame, text="Cantidad Vendida", borderwidth=2, relief="solid", width=20).pack(side='left', padx=2)
    
    # Mostrar los productos vendidos
    for producto in productos_mas_vendidos:
        producto_frame = Frame(analisis_frame)
        producto_frame.pack(fill='x', pady=2)
        
        Label(producto_frame, text=producto.getNombre(), borderwidth=1, relief="solid", width=20).pack(side='left', padx=2)
        Label(producto_frame, text=producto.getCantidadVendida(), borderwidth=1, relief="solid", width=20).pack(side='left', padx=2)
    
    def continuar_analisis(master_frame):
    # Limpiar el frame actual (el de análisis de mercadeo)
        for widget in master_frame.winfo_children():
            widget.destroy()

        # Ahora creamos el nuevo frame para el análisis de intercambio
        funerarias = Establecimiento.filtrarEstablecimiento("funeraria")
        analisis_intercambio(master_frame, funerarias, funeraria)
    # Botón para continuar
    continuar_button = Button(analisis_frame, text="Continuar", command=lambda: continuar_analisis(master_frame))
    continuar_button.pack(pady=10)


def analisis_intercambio(master_frame, funerarias, funeraria_origen):
    # Limpia el frame actual
    for widget in master_frame.winfo_children():
        widget.destroy()

    # Título del análisis de intercambio
    title_label = Label(master_frame, text="Análisis de Intercambio", font=('Helvetica', 16, 'bold'))
    title_label.pack(pady=20)

    # Mostrar productos disponibles en otras funerarias
    products_label = Label(master_frame, text="Productos Disponibles para Intercambio", font=('Helvetica', 14))
    products_label.pack(pady=10)

    # Crear un Frame para los productos
    products_frame = Frame(master_frame)
    products_frame.pack(pady=10)

    # Crear un diccionario para almacenar los widgets de productos
    product_widgets = {}

    # Recorrer las funerarias y mostrar sus productos
    for funeraria in funerarias:
        if funeraria != funeraria_origen:  # Evitar mostrar los productos de la funeraria de origen
            products = funeraria.getListadoProductosF()  # Obtén la lista de productos de la funeraria

            # Crear un Label para cada funeraria
            funeraria_label = Label(products_frame, text=f"Productos en {funeraria.getNombre()}", font=('Helvetica', 12, 'bold'))
            funeraria_label.pack(pady=5)

            # Crear un Frame para los productos de la funeraria
            individual_products_frame = Frame(products_frame)
            individual_products_frame.pack(pady=5)

            for producto in products:
                product_info = f"{producto.getNombre()} - Cantidad: {producto.getCantidad()}"
                product_label = Label(individual_products_frame, text=product_info)
                product_label.pack(anchor='w')

                # Añadir cada producto a un diccionario para su posible selección
                product_widgets[producto.getNombre()] = {
                    'label': product_label,
                    'producto': producto
                }

    # Función que se llama cuando el botón continuar es presionado
    def continuar_a_intercambio():
        # Obtener la funeraria de destino seleccionada (en este caso, la primera distinta a la de origen)
        funeraria_destino = next(f for f in funerarias if f != funeraria_origen)

        # Limpiar el frame actual
        for widget in master_frame.winfo_children():
            widget.destroy()

        # Llamar a la función de realizar intercambio
        realizar_intercambio(funeraria_origen, funeraria_destino, master_frame)

    # Botón para continuar con el análisis de intercambio
    continue_button = Button(master_frame, text="Continuar", command=continuar_a_intercambio)
    continue_button.pack(pady=20)


def realizar_intercambio(funeraria_origen, funeraria_destino, root):
    # Crear frame para el intercambio
    frame_intercambio = tk.Frame(root)
    frame_intercambio.pack(fill=tk.BOTH, expand=True)

    # Título
    titulo_label = tk.Label(frame_intercambio, text="Realizar Intercambio", font=('Helvetica', 16, 'bold'))
    titulo_label.pack(pady=10)

    # Selección de productos
    productos_origen = funeraria_origen.getListadoProductosF()
    productos_destino = funeraria_destino.getListadoProductosF()

    lista_productos_var = tk.StringVar()
    opciones_productos = [f"{p.getNombre()} (Stock: {p.getCantidad()})" for p in productos_origen]
    lista_productos = ttk.Combobox(frame_intercambio, textvariable=lista_productos_var, values=opciones_productos, state="readonly", width=30)
    lista_productos.pack(pady=10)

    cantidad_var = tk.IntVar()
    cantidad_label = tk.Label(frame_intercambio, text="Cantidad a transferir")
    cantidad_label.pack(pady=5)
    cantidad_entry = tk.Entry(frame_intercambio, textvariable=cantidad_var)
    cantidad_entry.pack(pady=5)

    # Confirmar selección de productos
    def confirmar_seleccion_producto():
        producto_seleccionado = lista_productos_var.get()
        cantidad_seleccionada = cantidad_var.get()

        if producto_seleccionado and cantidad_seleccionada > 0:
            # Actualizar el stock en las funerarias
            nombre_producto = producto_seleccionado.split(" (")[0]
            for p in productos_origen:
                if p.getNombre() == nombre_producto:
                    if p.getCantidad() >= cantidad_seleccionada:
                        p.setCantidad(p.getCantidad() - cantidad_seleccionada)
                        agregar_o_actualizar_producto(funeraria_destino, p, cantidad_seleccionada)
                        tk.messagebox.showinfo("Éxito", f"Producto {nombre_producto} transferido con éxito")
                    else:
                        tk.messagebox.showerror("Error", "Stock insuficiente")
                    break
        else:
            tk.messagebox.showerror("Error", "Debe seleccionar un producto y una cantidad válida")

    btn_confirmar_producto = tk.Button(frame_intercambio, text="Confirmar Producto", command=confirmar_seleccion_producto)
    btn_confirmar_producto.pack(pady=10)

    # Selección de empleados
    def seleccionar_empleados():
        seleccionarEmpleados(funeraria_origen,root)

    btn_seleccionar_empleado = tk.Button(frame_intercambio, text="Seleccionar Empleado", command=seleccionar_empleados)
    btn_seleccionar_empleado.pack(pady=10)

    # Selección de vehículos
    def seleccionar_vehiculos():
        seleccionarVehiculos(funeraria_origen,root)

    btn_seleccionar_vehiculo = tk.Button(frame_intercambio, text="Seleccionar Vehículo", command=seleccionar_vehiculos)
    btn_seleccionar_vehiculo.pack(pady=10)

    # Finalizar intercambio
    def finalizar_intercambio(master_frame):
        tk.messagebox.showinfo("Intercambio Finalizado", "El intercambio se ha completado exitosamente")
        for widget in master_frame.winfo_children():
            widget.destroy()

        comprar_productos(master_frame,funeraria_origen)
        

    btn_finalizar = tk.Button(frame_intercambio, text="Finalizar Intercambio", command=lambda: finalizar_intercambio(root))
    btn_finalizar.pack(pady=20)

    # Cancelar intercambio
    def cancelar_intercambio():
        frame_intercambio.destroy()

    btn_cancelar = tk.Button(frame_intercambio, text="Cancelar", command=cancelar_intercambio)
    btn_cancelar.pack(pady=5)

def agregar_o_actualizar_producto(funeraria, producto, cantidad):
    productos_destino = funeraria.getListadoProductos()
    producto_encontrado = False

    for p in productos_destino:
        if p.getNombre() == producto.getNombre():
            p.setCantidad(p.getCantidad() + cantidad)
            producto_encontrado = True
            break

    if not producto_encontrado:
        nuevo_producto = Producto(producto.getNombre(), producto.getPrecio(), cantidad)
        funeraria.agregarProducto(nuevo_producto)

def seleccionarEmpleados(funeraria, frame):
    # Crear frame para la selección de empleados
    frame_empleados = Frame(frame)
    frame_empleados.pack(fill=tk.BOTH, expand=True)

    # Título
    titulo_label = tk.Label(frame_empleados, text="Seleccionar Empleado", font=('Helvetica', 16, 'bold'))
    titulo_label.pack(pady=10)

    # Lista para mostrar empleados disponibles
    lista_empleados_var = tk.StringVar()
    opciones_empleados = [empleado.getNombre() for empleado in funeraria.getEmpleados()]
    lista_empleados = ttk.Combobox(frame_empleados, textvariable=lista_empleados_var, values=opciones_empleados, state="readonly")
    lista_empleados.pack(pady=10)

    # Botón de confirmar selección
    def confirmar_seleccion_empleado():
        empleado_seleccionado = lista_empleados_var.get()
        if empleado_seleccionado:
            tk.messagebox.showinfo("Empleado Seleccionado", f"Empleado {empleado_seleccionado} seleccionado con éxito")
            frame_empleados.destroy()  # Limpiar el frame después de la selección
        else:
            tk.messagebox.showerror("Error", "Debe seleccionar un empleado")

    btn_confirmar_empleado = tk.Button(frame_empleados, text="Confirmar Selección", command=confirmar_seleccion_empleado)
    btn_confirmar_empleado.pack(pady=20)

    # Botón para cancelar la selección
    def cancelar_seleccion_empleado():
        frame_empleados.destroy()  # Limpiar el frame sin seleccionar ningún empleado

    btn_cancelar_empleado = tk.Button(frame_empleados, text="Cancelar", command=cancelar_seleccion_empleado)
    btn_cancelar_empleado.pack(pady=5)

def seleccionarVehiculos(funeraria,frame):
    # Crear frame para la selección de vehículos
    frame_vehiculos = Frame(frame)
    frame_vehiculos.pack(fill=tk.BOTH, expand=True)

    # Título
    titulo_label = tk.Label(frame_vehiculos, text="Seleccionar Vehículo", font=('Helvetica', 16, 'bold'))
    titulo_label.pack(pady=10)

    # Lista para mostrar vehículos disponibles
    lista_vehiculos_var = tk.StringVar()
    opciones_vehiculos = [f"{vehiculo.getPlaca()} - {vehiculo.getTipoVehiculo()}" for vehiculo in funeraria.getVehiculos()]
    lista_vehiculos = ttk.Combobox(frame_vehiculos, textvariable=lista_vehiculos_var, values=opciones_vehiculos, state="readonly",width=45)
    lista_vehiculos.pack(pady=10)

    # Botón de confirmar selección
    def confirmar_seleccion_vehiculo():
        vehiculo_seleccionado = lista_vehiculos_var.get()
        if vehiculo_seleccionado:
            tk.messagebox.showinfo("Vehículo Seleccionado", f"Vehículo {vehiculo_seleccionado} seleccionado con éxito")
            frame_vehiculos.destroy()  # Limpiar el frame después de la selección
        else:
            tk.messagebox.showerror("Error", "Debe seleccionar un vehículo")

    btn_confirmar_vehiculo = tk.Button(frame_vehiculos, text="Confirmar Selección", command=confirmar_seleccion_vehiculo)
    btn_confirmar_vehiculo.pack(pady=20)

    # Botón para cancelar la selección
    def cancelar_seleccion_vehiculo():
        frame_vehiculos.destroy()  # Limpiar el frame sin seleccionar ningún vehículo

    btn_cancelar_vehiculo = tk.Button(frame_vehiculos, text="Cancelar", command=cancelar_seleccion_vehiculo)
    btn_cancelar_vehiculo.pack(pady=5)

def comprar_productos(frame, funeraria):
    # Crear un frame dentro del frame principal para el proceso de compra
    frame_compra = tk.Frame(frame)
    frame_compra.pack(fill=tk.BOTH, expand=True)

    # Título de la compra
    titulo_label = tk.Label(frame_compra, text="Comprar Productos", font=('Helvetica', 16, 'bold'))
    titulo_label.pack(pady=10)

    # Mostrar productos con menos de 10 existencias
    productos_faltantes = funeraria.identificarProductosFaltantes(funeraria)
    productos_faltantes = [p for p in productos_faltantes if isinstance(p, Producto)]
    productos_faltantes = [p for p in productos_faltantes if isinstance(p.getCantidadVendida(), (int, float))]

    if not productos_faltantes:
        mensaje_label = tk.Label(frame_compra, text="No hay productos con menos de 10 existencias.", font=('Helvetica', 12))
        mensaje_label.pack(pady=10)
        return  # Salir de la función si no hay productos faltantes

    productos_label = tk.Label(frame_compra, text="Productos con menos de 10 existencias:", font=('Helvetica', 12))
    productos_label.pack(pady=5)

    lista_productos_var = tk.StringVar()
    opciones_productos = [f"{p.getNombre()} (Stock: {p.getCantidad()})" for p in productos_faltantes]
    lista_productos = ttk.Combobox(frame_compra, textvariable=lista_productos_var, values=opciones_productos, state="readonly")
    lista_productos.pack(pady=10)

    # Selección de proveedores
    proveedores = funeraria.getListadoProveedoresF()  # Obtener la lista de proveedores
    lista_proveedores_var = tk.StringVar()
    opciones_proveedores = [p.getNombre() for p in proveedores]
    lista_proveedores = ttk.Combobox(frame_compra, textvariable=lista_proveedores_var, values=opciones_proveedores, state="readonly")
    lista_proveedores.pack(pady=10)

    # Campo para cantidad de compra
    cantidad_var = tk.StringVar()  # Cambiar a StringVar para validación personalizada
    cantidad_label = tk.Label(frame_compra, text="Cantidad a comprar")
    cantidad_label.pack(pady=5)
    cantidad_entry = tk.Entry(frame_compra, textvariable=cantidad_var)
    cantidad_entry.pack(pady=5)

    # Confirmar compra
    def confirmar_compra():
        producto_seleccionado = lista_productos_var.get()
        proveedor_seleccionado = lista_proveedores_var.get()
        cantidad_comprada = cantidad_var.get()

        try:
            # Validar que la cantidad sea un número entero
            if not cantidad_comprada.isdigit():
                raise ValueError("La cantidad debe ser un número entero.")
        
            cantidad_comprada = int(cantidad_comprada)  # Convertir a entero si es válido

            # Comprobar que la cantidad no sea mayor a 100
            if cantidad_comprada > 100:
                raise ValueError("La cantidad comprada no puede ser mayor de 100.")

            if producto_seleccionado and proveedor_seleccionado:
                # Aquí podrías hacer algo más si fuera necesario
                messagebox.showinfo("Éxito", f"Compra de {cantidad_comprada} unidades de {producto_seleccionado} realizada con éxito.")
            else:
                messagebox.showerror("Error", "Debe seleccionar un producto y un proveedor.")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    btn_confirmar_compra = tk.Button(frame_compra, text="Confirmar Compra", command=confirmar_compra)
    btn_confirmar_compra.pack(pady=10)

    # Botón para finalizar la compra
    def finalizar_compra(master_frame, funeraria):
        tk.messagebox.showinfo("Compra Finalizada", "La compra se ha completado exitosamente.")
        for widget in master_frame.winfo_children():
            widget.destroy()
        calificarProceso(frame, funeraria)
        

    btn_finalizar = tk.Button(frame_compra, text="Finalizar Compra",command=lambda: finalizar_compra(frame, funeraria))
    btn_finalizar.pack(pady=10)

    # Botón para cancelar
    def cancelar_compra():
        frame_compra.destroy()

    btn_cancelar = tk.Button(frame_compra, text="Cancelar", command=cancelar_compra)
    btn_cancelar.pack(pady=5)

    # Botón para comprar vehículos
    def abrir_comprar_vehiculos():
        comprarVehiculos(frame, funeraria)

    btn_comprar_vehiculos = tk.Button(frame_compra, text="Comprar Vehículos", command=abrir_comprar_vehiculos)
    btn_comprar_vehiculos.pack(pady=5)

    # Botón para contratar empleados
    def abrir_contratar_empleados():
        contratarEmpleados(frame, funeraria)

    btn_contratar_empleados = tk.Button(frame_compra, text="Contratar Empleados", command=abrir_contratar_empleados)
    btn_contratar_empleados.pack(pady=5)

def contratarEmpleados(frame, funeraria):
    # Crear un nuevo frame para el proceso de contratación de empleados
    frame_contratar = tk.Frame(frame)
    frame_contratar.pack(fill=tk.BOTH, expand=True)

    # Titulo de la contratacion
    titulo_label = tk.Label(frame_contratar, text="Contratar Empleados", font=('Helvetica', 16, 'bold'))
    titulo_label.pack(pady=10)

    # Obtener los proveedores de empleados de la funeraria
    proveedores_empleados = funeraria.getListadoProveedoresEmpleadosF()

    if not proveedores_empleados:
        mensaje_label = tk.Label(frame_contratar, text="No hay proveedores de empleados disponibles.", font=('Helvetica', 12))
        mensaje_label.pack(pady=10)
        return  # Salir de la función si no hay proveedores disponibles

    proveedores_label = tk.Label(frame_contratar, text="Selecciona un proveedor de empleados:", font=('Helvetica', 12))
    proveedores_label.pack(pady=5)

    lista_proveedores_var = tk.StringVar()
    opciones_proveedores = [p.getNombre() for p in proveedores_empleados]
    lista_proveedores = ttk.Combobox(frame_contratar, textvariable=lista_proveedores_var, values=opciones_proveedores, state="readonly")
    lista_proveedores.pack(pady=10)

    
    # Mostrar empleados del proveedor seleccionado
    empleados_label = tk.Label(frame_contratar, text="Empleados disponibles para contratar:", font=('Helvetica', 12))
    empleados_label.pack(pady=5)

    lista_empleados_var = tk.StringVar()
    lista_empleados = ttk.Combobox(frame_contratar, textvariable=lista_empleados_var, state="readonly")
    lista_empleados.pack(pady=10)

    # Funcion para mostrar empleados según el proveedor seleccionado
    def mostrar_empleados():
        proveedor_seleccionado = lista_proveedores_var.get()

        if proveedor_seleccionado:
            for proveedor in proveedores_empleados:
                if proveedor.getNombre() == proveedor_seleccionado:
                    # Usar la función seleccionarEmpleados para obtener la lista de empleados del proveedor
                    empleados_disponibles = proveedor.getEmpleados()

                    # Actualizar el combobox de empleados
                    opciones_empleados = [e.getNombre() for e in empleados_disponibles]
                    lista_empleados['values'] = opciones_empleados
                    lista_empleados_var.set('')  # Limpiar selección previa

                    if not empleados_disponibles:
                        tk.messagebox.showinfo("Información", "Este proveedor no tiene empleados disponibles para contratar.")
                    break

    # Asociar la función mostrar_empleados al evento de selección del proveedor
    lista_proveedores.bind("<<ComboboxSelected>>", lambda event: mostrar_empleados())

    # Confirmar contratación
    def confirmar_contratacion():
        empleado_seleccionado = lista_empleados_var.get()
        proveedor_seleccionado = lista_proveedores_var.get()

        if empleado_seleccionado and proveedor_seleccionado:
            # Buscar el proveedor y el empleado seleccionado
            for proveedor in proveedores_empleados:
                if proveedor.getNombre() == proveedor_seleccionado:
                    empleados_disponibles = proveedor.getEmpleados()
                    for empleado in empleados_disponibles:
                        if empleado.getNombre() == empleado_seleccionado:
                            # Contratar al empleado y agregarlo a la lista de empleados de la funeraria
                            funeraria.getEmpleados().append(empleado)
                            tk.messagebox.showinfo("Éxito", f"Empleado {empleado_seleccionado} contratado exitosamente.")
                            return

        tk.messagebox.showerror("Error", "Debe seleccionar un empleado válido para contratar.")

    # Botón para confirmar la contratación
    btn_confirmar_contratacion = tk.Button(frame_contratar, text="Confirmar Contratación", command=confirmar_contratacion)
    btn_confirmar_contratacion.pack(pady=10)

    # Botón para finalizar contratación
    def finalizar_contratacion():
        tk.messagebox.showinfo("Proceso finalizado", "La contratación ha sido completada.")
        frame_contratar.destroy()

    btn_finalizar = tk.Button(frame_contratar, text="Finalizar", command=finalizar_contratacion)
    btn_finalizar.pack(pady=10)

    # Botón para cancelar
    def cancelar_contratacion():
        frame_contratar.destroy()

    btn_cancelar = tk.Button(frame_contratar, text="Cancelar", command=cancelar_contratacion)
    btn_cancelar.pack(pady=5)

def comprarVehiculos(frame, funeraria):
    # Crear un nuevo frame para la compra de vehículos
    frame_comprar = tk.Frame(frame)
    frame_comprar.pack(fill=tk.BOTH, expand=True)

    # Título de la compra de vehículos
    titulo_label = tk.Label(frame_comprar, text="Comprar Vehículos", font=('Helvetica', 16, 'bold'))
    titulo_label.pack(pady=10)

    # Obtener los proveedores de vehículos de la funeraria
    proveedores_vehiculos = funeraria.getListadoProveedoresVehiculos()

    if not proveedores_vehiculos:
        mensaje_label = tk.Label(frame_comprar, text="No hay proveedores de vehículos disponibles.", font=('Helvetica', 12))
        mensaje_label.pack(pady=10)
        return  # Salir de la función si no hay proveedores disponibles

    proveedores_label = tk.Label(frame_comprar, text="Selecciona un proveedor de vehículos:", font=('Helvetica', 12))
    proveedores_label.pack(pady=5)

    lista_proveedores_var = tk.StringVar()
    opciones_proveedores = [p.getNombre() for p in proveedores_vehiculos]
    lista_proveedores = ttk.Combobox(frame_comprar, textvariable=lista_proveedores_var, values=opciones_proveedores, state="readonly")
    lista_proveedores.pack(pady=10)

    # Mostrar vehículos del proveedor seleccionado
    vehiculos_label = tk.Label(frame_comprar, text="Vehículos disponibles para comprar:", font=('Helvetica', 12))
    vehiculos_label.pack(pady=5)

    lista_vehiculos_var = tk.StringVar()
    lista_vehiculos = ttk.Combobox(frame_comprar, textvariable=lista_vehiculos_var, state="readonly")
    lista_vehiculos.pack(pady=10)

    # Función para mostrar vehículos según el proveedor seleccionado
    def mostrar_vehiculos():
        proveedor_seleccionado = lista_proveedores_var.get()

        if proveedor_seleccionado:
            for proveedor in proveedores_vehiculos:
                if proveedor.getNombre() == proveedor_seleccionado:
                    # Usar la función seleccionarVehiculos para obtener la lista de vehículos del proveedor
                    vehiculos_disponibles = proveedor.getVehiculos()

                    # Actualizar el combobox de vehículos
                    opciones_vehiculos = [v.getPlaca() for v in vehiculos_disponibles]
                    lista_vehiculos['values'] = opciones_vehiculos
                    lista_vehiculos_var.set('')  # Limpiar selección previa

                    if not vehiculos_disponibles:
                        tk.messagebox.showinfo("Información", "Este proveedor no tiene vehículos disponibles para comprar.")
                    break

    # Asociar la función mostrar_vehiculos al evento de selección del proveedor
    lista_proveedores.bind("<<ComboboxSelected>>", lambda event: mostrar_vehiculos())

    # Confirmar compra
    def confirmar_compra():
        vehiculo_seleccionado = lista_vehiculos_var.get()
        proveedor_seleccionado = lista_proveedores_var.get()

        if vehiculo_seleccionado and proveedor_seleccionado:
            # Buscar el proveedor y el vehículo seleccionado
            for proveedor in proveedores_vehiculos:
                if proveedor.getNombre() == proveedor_seleccionado:
                    vehiculos_disponibles = proveedor.getVehiculos()
                    for vehiculo in vehiculos_disponibles:
                        if vehiculo.getPlaca() == vehiculo_seleccionado:
                            # Comprar el vehículo y agregarlo a la lista de vehículos de la funeraria
                            funeraria.getVehiculos().append(vehiculo)
                            tk.messagebox.showinfo("Éxito", f"Vehículo {vehiculo_seleccionado} comprado exitosamente.")
                            return

        tk.messagebox.showerror("Error", "Debe seleccionar un vehículo válido para comprar.")

    # Botón para confirmar la compra
    btn_confirmar_compra = tk.Button(frame_comprar, text="Confirmar Compra", command=confirmar_compra)
    btn_confirmar_compra.pack(pady=10)

    # Botón para finalizar la compra
    def finalizar_compra():
        tk.messagebox.showinfo("Proceso finalizado", "La compra ha sido completada.")
        frame_comprar.destroy()

    btn_finalizar = tk.Button(frame_comprar, text="Finalizar", command=finalizar_compra)
    btn_finalizar.pack(pady=10)

    # Botón para cancelar
    def cancelar_compra():
        frame_comprar.destroy()

    btn_cancelar = tk.Button(frame_comprar, text="Cancelar", command=cancelar_compra)
    btn_cancelar.pack(pady=5)

def calificarProceso(frame, funeraria):
    # Crear un frame para el proceso de calificación
    frame_calificacion = tk.Frame(frame)
    frame_calificacion.pack(fill=tk.BOTH, expand=True)

    # Título de la calificación
    titulo_label = tk.Label(frame_calificacion, text="Calificación del Proceso", font=('Helvetica', 16, 'bold'))
    titulo_label.pack(pady=10)

    # Campo para la calificación (nota)
    calificacion_var = tk.StringVar()
    calificacion_label = tk.Label(frame_calificacion, text="Calificación (1-10):")
    calificacion_label.pack(pady=5)
    calificacion_entry = tk.Entry(frame_calificacion, textvariable=calificacion_var)
    calificacion_entry.pack(pady=5)

    # Campo para la descripción
    descripcion_label = tk.Label(frame_calificacion, text="Descripción del proceso:")
    descripcion_label.pack(pady=5)
    
    descripcion_text = tk.Text(frame_calificacion, height=5, width=40)  
    descripcion_text.pack(pady=5)

    # Función para validar y finalizar la calificación
    def finalizar_calificacion():
        calificacion = calificacion_var.get()
        descripcion = descripcion_text.get("1.0", tk.END).strip()

        try:
            # Validar que haya una calificación
            if not calificacion:
                raise CalificacionIncompleta()

            # Validar que haya una descripción
            if not descripcion:
                raise DescripcionIncompleta()

            
            funeraria.setCalificacion(calificacion) 
            funeraria.setDescripcion(descripcion)

            tk.messagebox.showinfo("Finalizado", "Gracias por calificar el proceso. Proceso finalizado.")
            frame_calificacion.destroy()  # Destruir el frame al finalizar
        except CamposIncompletos as e:
            tk.messagebox.showerror("Error", str(e))

    
    btn_finalizar = tk.Button(frame_calificacion, text="Finalizar", command=finalizar_calificacion)
    btn_finalizar.pack(pady=10)
