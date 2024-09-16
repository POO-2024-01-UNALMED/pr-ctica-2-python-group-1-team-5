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
                pass
            
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
    facturas = funeraria.getFacturasPorPagar()
    global current_frame,separador
    if current_frame:
        current_frame.destroy()
    if separador:
        separador.destroy()
    frameSeparador=tk.Frame(frame)
    frameSeparador.pack(pady=10)
    if(len(facturas) > 0):
        valorFactura = frame1(frame,["Facturas"],[facturas])

    else:
        tk.messagebox.showinfo("", "No hay facturas disponibles en la funeraria")
        funcionalidadFinanzas(frame)

    btnContinuar= tk.Button(frame,text="Continuar",)
    btnContinuar.pack(side="top",pady=10)



    

def pagoEmpleados(frame,funeraria):
    pass
def credito(frame,funeraria):
    pass
def reajusteDinero(frame,funeraria):
    pass




