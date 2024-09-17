from gestorAplicacion.inventario.urna import Urna
from gestorAplicacion.inventario.tumba import Tumba
from gestorAplicacion.establecimientos.establecimiento import Establecimiento
from gestorAplicacion.establecimientos.cementerio import Cementerio
from gestorAplicacion.establecimientos.iglesia import Iglesia

import tkinter as tk
from iuMain.frame import frame1
from iuMain.frame import FieldFrame
from iuMain.frame import tablas
from iuMain.manejoErrores.errorAplicacion import errorNumeros
from iuMain.manejoErrores.errorAplicacion import errorIds
from iuMain.manejoErrores.errorAplicacion import errorPeso
from iuMain.manejoErrores.errorAplicacion import errorEstatura
from iuMain.manejoErrores.errorAplicacion import clienteIncompleto
# Se usa para borrar lo que hay en el frame y mostrar el titulo de la funcionalidad

def titulo(frame,titulo):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text=titulo, bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

def funcionalidadExhumacion(frame):
    cliente = None
    urnaTumba = None
    cementerio = None
    nuevaUrnaTumba = None

    titulo(frame,"Servicio de Exhumación")
    
    # Breve descripción de la funcionalidad para los usuarios
    etiqueta = tk.Label(frame, text="La exhumación es el proceso de retirar un cuerpo de su lugar de sepultura")
    etiqueta.pack(pady=2)
    etiqueta1 = tk.Label(frame, text="Ingrese los siguientes datos para la búsqueda del Cliente")
    etiqueta1.pack(pady=4)
    funerarias = Establecimiento.filtrarEstablecimiento("funeraria")
    listaCliente=["Mayor de edad","Menor de edad"]
    listaBuscar=["Cementerios de cuerpos","Urna default","Tumba default"]
   
    datoInicio = frame1(frame,["Seleccione la funeraria: ","Buscar Cliente en: ","Cliente: "],[funerarias,listaBuscar,listaCliente])

    def datosInicio():
        if datoInicio.continuar():
            funeraria=funerarias[(datoInicio.getValores())[0]]
           
            buscar=listaBuscar[(datoInicio.getValores())[1]]
          
            tipoCliente=listaCliente[(datoInicio.getValores())[2]]
            
            datoInicio.bloquearOpciones()
            btnContinuar.destroy()
            seleccionCliente(frame,funeraria,buscar,tipoCliente)
    btnContinuar= tk.Button(frame,text="Continuar", command=lambda:datosInicio())
    btnContinuar.pack(side="top",pady=10)


def seleccionCliente(frame,funeraria,buscar,tipoCliente):
    
    separador=tk.Frame(frame)
    separador.pack(pady=10)

    clientes=[]
    tipo = None
    mensaje1 = None
    mensaje2 = None
    
    if buscar == "Cementerios de cuerpos":
        if tipoCliente == "Mayor de edad":
            clientes = funeraria.buscarClienteCementerio("cuerpos", "adulto")
            
        else:
            clientes = funeraria.buscarClienteCementerio("cuerpos", "niño")
        
        opciones=["cementerio cenizas","cementerio cuerpos"]
        frameCliente=frame1(frame,[f"Clientes {tipoCliente}","Opciones para traslado"],[clientes,opciones])
    else:
        opciones=["cementerio cenizas"]    
        if buscar =="Urna default":
            tipo = "cenizas"
            mensaje2 = "Urnitas"
        else:
            tipo = "cuerpos"
            mensaje1 = "Cementerios de cuerpos"
            opciones.append("cementerio cuerpos")
            mensaje2 = "Tumbitas"
        
                
        # Se traen todos los cementerios por funeraria
        cementeriosPorFuneraria = Establecimiento.buscarPorFuneraria(funeraria, "cementerio")
        # Se traen todos los cementerios de la funeraria con el atributo de tipo correspondiente ("cuerpos" o "cenizas")
        cementerios = Cementerio.cementerioPorTipo(cementeriosPorFuneraria, tipo)

        for auxCementerio in cementerios:
            if len(auxCementerio.inventarioDefault()) ==0:
                cementerios.remove(auxCementerio)

        frameCementerios=frame1(frame,[f"Cementerios {tipo}","Opciones para traslado"],[cementerios,opciones])

    
    
    def porInventario(entradaInventario,inventarioDefault,traslado):
        if entradaInventario.continuar():
            num=0
            try:             
                urnaTumba=inventarioDefault[int(entradaInventario.getValores()[0])]
                if int(entradaInventario.getValores()[0])<0:
                        errorIds(inventarioDefault[int(entradaInventario.getValores()[0])],"El ID ingresado es incorrecto",0,len(urnaTumba)-1)
                cliente=urnaTumba.getCliente()
                num=1

            except:
                
                errorIds(entradaInventario.getValores()[0],"El ID ingresado no es correcto")
                entradaInventario.borrar()
            if num==1:
                texto=f"Has seleccionado al cliente {cliente}\n ¿Deseas continuar?"
                result = tk.messagebox.askyesno("Confirmar Datos",texto)
                if result:
                    siguiente(frame,cliente,traslado)
                else:
                    clienteIncompleto()
                    frameCementerios.desbloquearOpciones()
                
    def establecerCliente():
        if buscar=="Cementerios de cuerpos":
            if frameCliente.continuar():
                frameCliente.bloquearOpciones()
                cliente=clientes[(frameCliente.getValores())[0]]
                texto=f"Has seleccionado al cliente {cliente} desde cementerio: {(cliente.getInventario()).getCementerio()}\n ¿Deseas continuar?"
                result = tk.messagebox.askyesno("Confirmar Datos",texto)

                traslado=None
                
                if (opciones[frameCliente.getValores()[1]])=="cementerio cuerpos":
                    traslado="cuerpos" 
                else: 
                    traslado="cenizas"

                if result:
                    siguiente(frame,cliente,traslado)
                else:
                    clienteIncompleto()
                    frameCliente.desbloquearOpciones()
                   
        else:
            if frameCementerios.continuar():
                #Poner un mesageBox 

                #Valor de traslado
                traslado=None
                if (opciones[frameCementerios.getValores()[1]])=="cementerio cuerpos":
                    traslado="cuerpos" 
                else: 
                    traslado="cenizas"

                frameCementerios.bloquearOpciones()
                btnContinuar.destroy()
                cementerio=cementerios[(frameCementerios.getValores())[0]]
                inventarioDefault = cementerio.inventarioDefault()
                nombres=list(map(lambda e: e.getNombre(),inventarioDefault))
                
                clientesInventario=list(map(lambda e: e.getCliente(),inventarioDefault))
                IDs=list(a for a in range(len(inventarioDefault)))
                separador = tk.Frame(frame)
                separador.pack(pady=2)
                if buscar=="Urna default":
                    tipos=list(map(lambda e: e.getTipo(),inventarioDefault))
                    tablas(frame,[mensaje2,"Cliente","Tipo","ID"],[nombres,clientesInventario,tipos,IDs])
                else:
                    tablas(frame,[mensaje2,"Cliente","ID"],[nombres,clientesInventario,IDs])
                entradaInventario=FieldFrame(frame,[],[f"Indique el ID de la {mensaje2}"])
                btnContinuar1= tk.Button(frame,text="Continuar", command=lambda:porInventario(entradaInventario,inventarioDefault,traslado))
                btnContinuar1.pack(side="top",pady=10)


    btnContinuar= tk.Button(frame,text="Continuar", command=lambda:establecerCliente())
    btnContinuar.pack(side="top",pady=10)


def siguiente(frame, cliente,traslado):
    titulo(frame,"Organización del traslado")
   
    # Iglesias disponibles
    iglesias = []
    iglesiasNombre=[]
    iglesiasReligion=[]
    

    if traslado == "cenizas":
        pesoEstatura = "Ingrese el peso del cliente (0-120) kg : "
        tipo1 = "cenizas"
        tipo2 = "urna"

        # Establecer iglesia para determinar religión del cliente 
        indice = 1
        maxIglesia = 0
        iglesias = []
        for auxIglesia in Iglesia:
            # Se imprimen y añaden a la lista solo las iglesias que permiten la cremación como acto final de la vida
            if auxIglesia.getCremacion():
                iglesias.append(auxIglesia)
                iglesiasNombre.append(auxIglesia.getNombre())
                iglesiasReligion.append(auxIglesia.name)
                indice += 1
                maxIglesia += 1

    else:
        pesoEstatura = "Ingrese la estatura del cliente (0-2)m: "
        tipo1 = "cuerpos"
        tipo2 = "tumba"

        # Establecer iglesia para determinar religión del cliente 
        maxIglesia = 0
        iglesias = []
        for auxIglesia in Iglesia:
            iglesias.append(auxIglesia)
            iglesiasNombre.append(auxIglesia.getNombre())
            iglesiasReligion.append(auxIglesia.name)
            maxIglesia += 1

    
    #Peso - estatura
    datosPesoEstatura= FieldFrame(frame,[],[pesoEstatura])
    tk.Label(frame,text="Seleccione la religión con la que se va a realizar la ceremonia del cliente").pack(side="top",pady=5)
    tablas(frame,["Religión","Nombre Iglesia","ID"],[iglesiasReligion,iglesiasNombre,list(map(lambda x: x, range(1, len(iglesiasNombre)+1)))])
    valorIglesia=FieldFrame(frame,[],["Indique el ID de la iglesia"])

    
    def organizacion():
        if datosPesoEstatura.continuar() and valorIglesia.continuar():
            num=0
            try:
            
                pesoEstatura1=float(datosPesoEstatura.getValores()[0])
                if traslado=="cenizas":
                    if float(pesoEstatura1)>120 or float(pesoEstatura1)<0:
                        errorPeso(pesoEstatura1,120)
                else:
                    if float(pesoEstatura1)>2 or float(pesoEstatura1)<0:
                        errorEstatura(pesoEstatura1,2)
                num=1
            except:
                errorPeso(datosPesoEstatura.getValores()[0],120)
            num=0
            try: 
            
                iglesia=iglesias[int(valorIglesia.getValores()[0])-1]
                
                num=1
            except:
                errorIds(valorIglesia.getValores()[0],"El ID ingresado no es válido")
        
            if num==1:
                nuevoCementerio1(frame,cliente,tipo1,tipo2,iglesia,pesoEstatura1)
            
        
    
    btnContinuar= tk.Button(frame,text="Continuar", command=lambda:organizacion())
    btnContinuar.pack(side="top",pady=10)


def nuevoCementerio1(frame,cliente,tipo1,tipo2,iglesia,pesoEstatura):
    titulo(frame,"Organización traslado")
    urnaTumba= cliente.getInventario()
    cementerio=urnaTumba.getCementerio()
    cementerio.setIglesia(iglesia)
    edad=cliente.getEdad()

    tk.Label(frame,text=f"El cliente {cliente} cuenta con una afiliación {cliente.getAfiliacion()}")

    cementeriosPorTipo = cementerio.getFuneraria().buscarCementerios(tipo1, cliente)

   

    # Elimino el cementerio en el que actualmente está el cliente
    try:
        cementeriosPorTipo.remove(cementerio)
    except:
        pass
    
    cementerios = []

    for auxCementerio in cementeriosPorTipo:
        auxCementerio.setIglesia(iglesia)
        if len(auxCementerio.disponibilidadInventario(tipo2, pesoEstatura, edad)) != 0:
            cementerios.append(auxCementerio)
           

    
    if len(cementerios) == 0:

        for auxCementerio in cementeriosPorTipo:
            if tipo1 == "cenizas":
                auxCementerio.agregarInventario(Urna("default", auxCementerio, pesoEstatura, edad, "fija"))

            else:
                auxCementerio.agregarInventario(Tumba("default", auxCementerio, pesoEstatura, edad))
            cementerios.append(auxCementerio)
           
        tk.messagebox.showinfo("Inventario disponible", "No se encontró inventario disponible para el cliente \n se deberá añadir inventario default")


    tk.Label(frame,text="Escoja ")
    inventarioDisponible= list(len(a.disponibilidadInventario(tipo2,pesoEstatura,edad)) for a in cementerios)
    IDs= list(map(lambda x: x, range(0, len(cementerios))))
    tablas(frame,["Cementerio","Inventario dispo","ID"],[cementerios,inventarioDisponible,IDs])
    valorCementerio=FieldFrame(frame,[],["Indique el ID del Cementerio"])


    def organizarDatos(cementerios):
        if valorCementerio.continuar():
            num=0
           
            try:
                
                nuevoCementerio=cementerios[int(valorCementerio.getValores()[0])]
                num=1
            except:
                errorIds(valorCementerio.getValores()[0],"Id incorrecta",0,1)
            
            if num==1:
                # Eliminar cliente
                try:
                    (nuevoCementerio.getClientes()).remove(cliente)
                except:
                    pass
                if len(nuevoCementerio.disponibilidadInventario(tipo2,pesoEstatura,edad)) ==1:
                    tk.messagebox.showinfo("Inventario Disponible", f"El cementerio seleccionado solo tiene una {tipo2} disponible\n El cliente {cliente} se agregará a la {tipo2} {nuevoCementerio.disponibilidadInventario(tipo2,pesoEstatura,edad)[0]}")
                    inventarioescogido=nuevoCementerio.disponibilidadInventario(tipo2,pesoEstatura,edad)[0]
                    organizarIglesia1(frame,nuevoCementerio,cliente,inventarioescogido)
                    
                else:
                    respuesta = tk.messagebox.askyesno("Inventario Recomendado", f"Se encontró la opción más adecuada en cuanto a tamaño \n Desea agregar trasladar al cliente a esta {tipo2}")
                    ventanaInventario = tk.Toplevel()
                    ventanaInventario.title("Funeraria Rosario")
                    ventanaInventario.geometry("400x200")
                    label = tk.Label(ventanaInventario, text=f"Cementerio {nuevoCementerio.getNombre()}", padx=10, anchor="w", wraplength=480)
                    label.pack(pady=2)
                    if respuesta:
                        urna =nuevoCementerio.inventarioRecomendado(nuevoCementerio.disponibilidadInventario(tipo2, pesoEstatura, edad))
                        print("Urnaaa",urna)
                        tablas(ventanaInventario,[f"{tipo2}","Tipo"],[[urna],[urna.getTipo()]])
                        btnContinuar= tk.Button(ventanaInventario,text="Continuar", command=lambda:organizarIglesia1(frame,nuevoCementerio,cliente,urna,ventanaInventario))
                        btnContinuar.pack(side="top",pady=10)
                    else:
                        dispoInventario = nuevoCementerio.disponibilidadInventario(tipo2, pesoEstatura, edad)
                        urna=nuevoCementerio.inventarioRecomendado(nuevoCementerio.disponibilidadInventario(tipo2, pesoEstatura, edad))
                        (dispoInventario).remove(urna)

                        cementerios= list(map(lambda p: p.getCementerio().getNombre(), dispoInventario))
                        tipos = list(map(lambda e: e.getTipo(),dispoInventario))
                        IDs=list(p for p in range(0,len(dispoInventario)))
                        tablas(ventanaInventario,[f"{tipo2}","Tipo","IDs"],[dispoInventario,tipos,IDs])
                        inventarioescogido = frame1(ventanaInventario,[f"Indique {tipo2} deseada"],[IDs])

                        btnContinuar= tk.Button(ventanaInventario,text="Continuar", command=lambda: organizarIglesia1(frame,nuevoCementerio,cliente,inventarioescogido,ventanaInventario))
                        btnContinuar.pack(side="top",pady=10)
                        


   
    btnContinuar= tk.Button(frame,text="Continuar", command=lambda:organizarDatos(cementerios))
    btnContinuar.pack(side="top",pady=10)


def organizarIglesia1(frame,nuevoCementerio,cliente,inventarioEscogido,ventanaInventario=None):
    
    try:
        inventarioEscogido.agregarCliente()
    except:
        pass

    if ventanaInventario!=None:
        ventanaInventario.destroy()
        
    titulo(frame,"Organización de los familiares dentro de la iglesia")
    iglesia =nuevoCementerio.organizarIglesia(cliente)

    frameApoyo = tk.Frame(frame, bg="#772d2d")
    frameApoyo.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    invitacion = tk.Label(frameApoyo, text=iglesia,font=("Comic Sans MS", 14, "italic"), bg="white")
    invitacion.pack(pady=50)

    from iuMain.ventanaPrincipal import framePrincipal
    boton_regresar = tk.Button(frameApoyo, text="Regresar", command=lambda: framePrincipal(frame))
    boton_regresar.pack()

   
    

     ###########################################################################
    
   
