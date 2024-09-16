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
from iuMain.frame import frame1
from iuMain.frame import FieldFrame
from iuMain.frame import tablas
from iuMain.manejoErrores.errorAplicacion import errorNumeros

current_frame = None
separador = None

# Se usa para borrar lo que hay en el frame y mostrar el titulo de la funcionalidad

def titulo(frame,titulo):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text=titulo, bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

def funcionalidadFinanzas(frame):

    titulo(frame, "Servicio de finanzas")
    funerarias= Establecimiento.filtrarEstablecimiento("funeraria")
    listaServicios=["Cobro clientes","Pagar Facturas","Pago empleados","Credito","Reajuste de dinero"]
    valores = frame1(frame,["Funeraria: ","Servicios: "],[funerarias,listaServicios])
    def datosInicio():
        if valores.continuar():
            funerarias = Establecimiento.filtrarEstablecimiento("funeraria")
            funeraria=funerarias[(valores.getValores())[0]]
            indiceServicios = listaServicios[valores.getValores()[1]]
            print(indiceServicios)
            if indiceServicios == "Cobro clientes":
                cobroClientes(frame,funeraria)

            elif indiceServicios == "Pagar Facturas":
                pagoFacturas(frame,funeraria)

            
            elif indiceServicios == "Pago empleados":
                pagoEmpleados(frame,funeraria)
            
            elif indiceServicios == "Credito":
                sCredito(frame,funeraria)

            elif indiceServicios == "Reajuste de dinero":
                reajusteDinero(frame,funeraria)
            
            btnContinuar.destroy()
    btnContinuar= tk.Button(frame,text="Continuar", command=lambda:datosInicio())
    btnContinuar.pack(side="top",pady=10)

def cobroClientes(frame,funeraria):
    titulo(frame, "Cobro clientes")
    texto= tk.Label(frame,text=f"Los cementerios disponibles para la funeraria {funeraria.getNombre()} son:")
    texto.pack(side="top",pady=5)
    cementerios = funeraria.cementerios()
    etiqueta = ["Cementerios"]
    global current_frame,separador
    if current_frame:
        current_frame.destroy()
    if separador:
        separador.destroy()
    frameSeparador=tk.Frame(frame)
    frameSeparador.pack(pady=10)
    valorCementerio = frame1(frame,etiqueta,[cementerios])
    def clientes(boton):
        if valorCementerio.continuar():
            valorCementerio.bloquearOpciones()
            boton.destroy()
            indice1000 = 0
            cementerio1 = cementerios[(valorCementerio.getValores())[0]]
            print(cementerio1)
            clientes = cementerio1.getClientes()
            clientesFacturas = []
            if(len(clientes) > 0):
                for cliente in clientes:
                    if(len(cliente.getListadoFacturas()) > 0):
                        indice1000 += 1
                        clientesFacturas.append(cliente)
        
            if(indice1000 == 0):
                tk.messagebox.showinfo("", "No hay clientes con facturas disponibles")
                funcionalidadFinanzas(frame)

            else:
                texto= tk.Label(frame,text=f"Los clientes disponibles para el cementerio {cementerio1.getNombre()} son:")
                texto.pack(side="top",pady=5)
                valoresClientes=frame1(frame,["Clientes"],[clientesFacturas])
                frameSeparador=tk.Frame(frame)
                frameSeparador.pack(pady=10)
                def cobroCliente():
                    cliente = clientesFacturas[(valoresClientes.getValores())[0]]
                    funeraria.cobroServiciosClientes(cliente)
                    texto = "Cobro de  facturas del cliente: "+ cliente.getNombre()+", realizado correctamente"
                    tk.messagebox.showinfo("",texto)
                    funcionalidadFinanzas(frame)


                btnContinuar= tk.Button(valoresClientes,text="Continuar", command=lambda:cobroCliente())
                btnContinuar.grid(row=1, column=2)
        
    btnContinuar= tk.Button(frame,text="Continuar", command=lambda:clientes(btnContinuar))
    btnContinuar.pack(side="top",pady=10)

def pagoFacturas(frame, funeraria):
    titulo(frame, "Pago Facturas")
    texto= tk.Label(frame,text=f"Las facturas disponibles para la funeraria {funeraria.getNombre()} son:")
    texto.pack(side="top",pady=5)
    facturas1 = funeraria.getFacturasPorPagar()
    global current_frame,separador
    if current_frame:
        current_frame.destroy()
    if separador:
        separador.destroy()
    frameSeparador=tk.Frame(frame)
    frameSeparador.pack(pady=10)
    if(len(facturas1) > 0):
        valorFactura = frame1(frame,["Facturas"],[facturas1])
        def facturas():
            factura = facturas1[(valorFactura.getValores())[0]]
            texto = funeraria.cobroFacturas(factura)
            tk.messagebox.showinfo("",texto)
            funcionalidadFinanzas(frame)
            
    else:
        tk.messagebox.showinfo("", "No hay facturas disponibles en la funeraria")
        funcionalidadFinanzas(frame)

    btnContinuar= tk.Button(frame,text="Continuar",command=lambda:facturas())
    btnContinuar.pack(side="top",pady=10)

def pagoEmpleados(frame,funeraria):
    titulo(frame,"Pago empleados")
    texto= tk.Label(frame,text=f"Las empleados a los que se les puede liquidar su pago en la funeraria {funeraria.getNombre()} son:")
    texto.pack(side="top",pady=5)
    empleados = funeraria.getEmpleados()
    global current_frame,separador
    if current_frame:
        current_frame.destroy()
    if separador:
        separador.destroy()
    frameSeparador=tk.Frame(frame)
    frameSeparador.pack(pady=10)
    empleadosDispo = []
    hayEmpleadosDispo = False

    for i in range(len(empleados)):
        empleado = empleados[i]
        if(empleado.getTrabajosHechos() > 0):
            empleadosDispo.append(empleado) 
            hayEmpleadosDispo = True

    if not hayEmpleadosDispo:
        tk.messagebox.showinfo("", "No hay empleados a los que se les pueda liquidar su pago en la funeraria")
        funcionalidadFinanzas(frame)
    
    else:
        valoresEmpleados=frame1(frame,["Empleados"],[empleadosDispo])
        def pago():
            empleado = empleadosDispo[(valoresEmpleados.getValores())[0]]
            texto = funeraria.pagoTrabajadores(empleado)
            tk.messagebox.showinfo("",texto)
            funcionalidadFinanzas(frame)

    
    btnContinuar= tk.Button(frame,text="Continuar",command=lambda:pago())
    btnContinuar.pack(side="top",pady=10)
    

def sCredito(frame,funeraria):
    titulo(frame, "Credito")
    texto= tk.Label(frame,text=f"Los servicios de credito disponibles en la funeraria {funeraria.getNombre()} son:")
    texto.pack(side="top",pady=5)
    global current_frame,separador
    if current_frame:
        current_frame.destroy()
    if separador:
        separador.destroy()
    frameSeparador=tk.Frame(frame)
    frameSeparador.pack(pady=10)
    listaServiciosCredito=["Pedir credito","Pago credito","Ver credito"]
    valoresCredito = frame1(frame,["Servicios credito: "],[listaServiciosCredito])
    def opciones(boton):
        if valoresCredito.continuar():
            valoresCredito.bloquearOpciones()
            boton.destroy()
            indiceServiciosCredito = listaServiciosCredito[valoresCredito.getValores()[0]]
            if indiceServiciosCredito == "Pedir credito":
                texto = funeraria.pedirCredito()
                tk.messagebox.showinfo("",texto)
                funcionalidadFinanzas(frame)
            
            elif indiceServiciosCredito == "Pago credito":

                creditos = funeraria.getCuentaCorriente().getCredito()

                if len(creditos) > 0:
                    texto= tk.Label(frame,text=f"Los creditos activos en la {funeraria.getNombre()} son:")
                    texto.pack(side="top",pady=5)
                    facturasCredito = frame1(frame,["Credito activos: "],[creditos])
                    def pC(boton):
                        facturasCredito.bloquearOpciones()
                        boton.destroy()
                        credito = creditos[(facturasCredito.getValores())[0]]
                        texto= tk.Label(frame,text=f"Que porcentaje del credito desea pagar ")
                        texto.pack(side="top",pady=5)
                        listaPorcentajes=["100%","80%","60%","40%","20%"]
                        valoresPorcentajes = frame1(frame,["Servicios credito: "],[listaPorcentajes])
                        def pCA(boton):
                            facturasCredito.bloquearOpciones()
                            boton.destroy()
                            indicePorcentaje = listaPorcentajes[(valoresPorcentajes.getValores())[0]]
                            iC = creditos.index(credito)
                            if indicePorcentaje == "100%":
                                texto = funeraria.pagarCredito(iC,1.0)
                                tk.messagebox.showinfo("",texto)

                            elif indicePorcentaje == "80%":
                                texto = funeraria.pagarCredito(iC,0.8)
                                tk.messagebox.showinfo("",texto)

                            elif indicePorcentaje == "60%":
                                texto = funeraria.pagarCredito(iC,0.6)
                                tk.messagebox.showinfo("",texto)

                            elif indicePorcentaje == "40%":
                                texto = funeraria.pagarCredito(iC,0.4)
                                tk.messagebox.showinfo("",texto)

                            elif indicePorcentaje == "20%":
                                texto = funeraria.pagarCredito(iC,0.2)
                                tk.messagebox.showinfo("",texto)
                            
                            funcionalidadFinanzas(frame)

                        btnContinuar= tk.Button(frame,text="Continuar",command=lambda:pCA(btnContinuar))
                        btnContinuar.pack(side="top",pady=10)

                    btnContinuar1= tk.Button(frame,text="Continuar",command=lambda:pC(btnContinuar1))
                    btnContinuar1.pack(side="top",pady=10)
                 
                else: 
                    tk.messagebox.showinfo("","No hay creditos activos en la funeraria")
                    funcionalidadFinanzas(frame)
           
            elif indiceServiciosCredito == "Ver credito":

                creditos = funeraria.getCuentaCorriente().getCredito()

                if len(creditos) > 0:
                    texto= tk.Label(frame,text=f"Los creditos activos en la {funeraria.getNombre()} son:")
                    texto.pack(side="top",pady=5)
                    facturasCredito2 = frame1(frame,["Credito activos: "],[creditos])
                    def credito3(boton):
                        facturasCredito2.bloquearOpciones()
                        boton.destroy()
                        credito = creditos[(facturasCredito2.getValores())[0]]
                        iC2 = creditos.index(credito)
                        texto = funeraria.getCuentaCorriente().infoCredito(iC2)
                        tk.messagebox.showinfo("Informe Credito",texto)
                        funcionalidadFinanzas(frame)

                    btnContinuar1= tk.Button(frame,text="Continuar",command=lambda:credito3(btnContinuar1))
                    btnContinuar1.pack(side="top",pady=10)
                 
                else: 
                 
                    tk.messagebox.showinfo("","No hay creditos activos en la funeraria")
                    funcionalidadFinanzas(frame)

    btnContinuar= tk.Button(frame,text="Continuar",command=lambda:opciones(btnContinuar))
    btnContinuar.pack(side="top",pady=10)

def reajusteDinero(frame,funeraria):
    titulo(frame, "Reajuste de dinero")
    texto= tk.Label(frame,text=f"Las empleados a los que se les puede liquidar su pago en la funeraria {funeraria.getNombre()} son:")
    texto.pack(side="top",pady=5)
    pass




