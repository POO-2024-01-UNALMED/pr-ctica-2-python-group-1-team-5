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
            print(funeraria)
            buscar=listaBuscar[(datoInicio.getValores())[1]]
            print(buscar)
            tipoCliente=listaCliente[(datoInicio.getValores())[2]]
            print(tipoCliente)
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
                print(nombres)
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
    print("yes")

    print("Traslado",traslado)
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
                    if float(pesoEstatura)>2 or float(pesoEstatura)<0:
                        errorEstatura(pesoEstatura,2)
                num=1
            except:
                errorPeso(datosPesoEstatura.getValores()[0],120)
            num=0
            try: 
                print(iglesias)
                print((valorIglesia.getValores()[0]))
                print("a")
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

    print(tipo1)
    print(cementerio)
    print(cliente)

    # Elimino el cementerio en el que actualmente está el cliente
    try:
        cementeriosPorTipo.remove(cementerio)
    except:
        pass
    print("Cementerios por tipo",cementeriosPorTipo)
    cementerios = []

    for auxCementerio in cementeriosPorTipo:
        auxCementerio.setIglesia(iglesia)
        if len(auxCementerio.disponibilidadInventario(tipo2, pesoEstatura, edad)) != 0:
            cementerios.append(auxCementerio)
            print("cementerios",auxCementerio)

    print(cementeriosPorTipo)
    if len(cementerios) == 0:

        for auxCementerio in cementeriosPorTipo:
            if tipo1 == "cenizas":
                auxCementerio.agregarInventario(Urna("default", auxCementerio, pesoEstatura, edad, "fija"))

            else:
                auxCementerio.agregarInventario(Tumba("default", auxCementerio, pesoEstatura, edad))
            cementerios.append(auxCementerio)
            print(auxCementerio)
        tk.messagebox.showinfo("Inventario disponible", "No se encontró inventario disponible para el cliente \n se deberá añadir inventario default")


    tk.Label(frame,text="Escoja ")
    inventarioDisponible= list(len(a.disponibilidadInventario(tipo2,pesoEstatura,edad)) for a in cementerios)
    IDs= list(map(lambda x: x, range(0, len(cementerios))))
    tablas(frame,["Cementerio","Inventario dispo","ID"],[cementerios,inventarioDisponible,IDs])
    valorCementerio=FieldFrame(frame,[],["Indique el ID del Cementerio"])


    def organizarDatos(cementerios):
        if valorCementerio.continuar():
            num=0
            print("valor",valorCementerio.getValores()[0])
            print("Cementerios ",cementerios)
            try:
                
                print("valor",valorCementerio.getValores()[0])
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
                    organizarIglesia(frame,nuevoCementerio,cliente,inventarioescogido)
                    
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
                        btnContinuar= tk.Button(ventanaInventario,text="Continuar", command=lambda:organizarIglesia(frame,nuevoCementerio,cliente,urna,ventanaInventario))
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

                        btnContinuar= tk.Button(ventanaInventario,text="Continuar", command=lambda: organizarIglesia(frame,nuevoCementerio,cliente,inventarioescogido,ventanaInventario))
                        btnContinuar.pack(side="top",pady=10)
                        


   
    btnContinuar= tk.Button(frame,text="Continuar", command=lambda:organizarDatos(cementerios))
    btnContinuar.pack(side="top",pady=10)


def organizarIglesia(frame,nuevoCementerio,cliente,inventarioEscogido,ventanaInventario=None):
    
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

    print(iglesia)
    

     ###########################################################################
    
   
"""
    # Obtener nuevo cementerio
    nuevoCementerio = cementerios[indice - 1]

    # Escoger opción más adecuada para cliente en cuánto a tamaño de la tumba comparado con estatura del cliente
    print(f"[1] Opción más adecuada en cuanto a tamaño: {nuevoCementerio.inventarioRecomendado(nuevoCementerio.disponibilidadInventario(tipo2, pesoEstatura, edad))}")
    print("[2] Buscar entre las otras opciones")

    # Ingreso del índice
    indice = int(input("Ingrese el índice correspondiente: "))

    # Validación de índice
    while indice < 1 or indice > 2:
        indice = int(input("El índice ingresado está fuera de rango. Ingrese nuevamente un índice: "))

    # Selección basada en el índice
    if indice == 1:
        nuevaUrnaTumba = nuevoCementerio.inventarioRecomendado(nuevoCementerio.disponibilidadInventario(tipo2, pesoEstatura, edad))
    elif indice == 2:
        disponible = nuevoCementerio.disponibilidadInventario(tipo2, pesoEstatura, edad)
        recomendacion = nuevoCementerio.inventarioRecomendado(nuevoCementerio.disponibilidadInventario(tipo2, pesoEstatura, edad))
        disponible.remove(recomendacion)
    
        # Imprimir opciones disponibles
        for i, auxInventario in enumerate(disponible, start=1):
            print(f"[{i}] {auxInventario}")
    
        # Ingreso del índice para la opción 2
        indice = int(input("Ingrese el índice correspondiente: "))
    
        # Validación de índice
        while indice < 1 or indice > len(disponible):
            indice = int(input("El índice ingresado está fuera de rango. Ingrese nuevamente un índice: "))
    
        nuevaUrnaTumba = disponible[indice - 1]

    #Asignacion de tumba
    nuevaUrnaTumba.agregarCliente(cliente)
	
    print(f"Se realizó correctamente el cambio al cementerio {nuevoCementerio}")
    urnaTumba.setCliente(None)

    nuevoCementerio.generarHoras()

    indice = 1
    for hora in nuevoCementerio.getHorarioEventos():
        indicador = "Pm" if int(hora[:2]) >= 12 else "Am"
        horaFormateada = hora  # Formato 12-horas con AM/PM
        print(f"[{indice}] {horaFormateada} {indicador}")
        indice += 1

    # Solicitar al usuario que ingrese el índice
    indice = int(input("Ingrese el índice para escoger el horario: "))

    #Se cambia el horario de crematorio
    nuevoCementerio.setHoraEvento(nuevoCementerio.getHorarioEventos()[indice-1])
    #Se elimina el horario de Horario eventos
    nuevoCementerio.eliminarHorario(nuevoCementerio.getHorarioEventos()[indice-1])

	#Seleccionar sepulturero
	
    print()
    print("Se inciará con el proceso de selección de empleados")
		
    print()
    print("Seleccione el empleado sepulturero disponible")

    print("Empleados disponibles en la jornada seleccionada")
    empleados =funeraria.buscarEmpleadosPorHoras(nuevoCementerio.getHoraEvento(), "sepulturero")
    indice = 1
    for auxEmpleado in empleados:
        print(f"[{indice}] {auxEmpleado}")
        indice += 1

    # Solicitar al usuario que ingrese el índice del empleado deseado
    indice = int(input("Ingrese el índice del empleado deseado: "))
    nuevoCementerio.setEmpleado(empleados[indice-1])

    print()
    print("Seleccione el empleado forense disponible")

    print("Empleados disponibles en la jornada seleccionada")
    empleados =funeraria.buscarEmpleadosPorHoras(nuevoCementerio.getHoraEvento(), "forense")
    indice = 1
    for auxEmpleado in empleados:
        print(f"[{indice}] {auxEmpleado}")
        indice += 1

    # Solicitar al usuario que ingrese el índice del empleado deseado
    indice = int(input("Ingrese el índice del empleado deseado: "))
    nuevoCementerio.setEmpleado(empleados[indice-1])
	
    #Seleccionar al padre u obispo 
    categoria=cliente.getInventario().getCategoria()
    empleado=None
    if(categoria==0):
        empleado="obispo"
    else: 
        empleado="padre"
	
    print(f"Dada la categoria [{categoria}] su ceremonia puede ser celebrada por los siguientes religiosos")
	
    empleados = cementerio.getFuneraria().buscarEmpleadosPorHoras(nuevoCementerio.getIglesia().duracionEvento(nuevoCementerio.getHoraEvento()), empleado)
 
    indice=1
    for auxEmpleado in empleados:
        if(categoria==0):
            print(f"[{indice}] {cementerio.getIglesia().getReligiosoAltoRango()} {auxEmpleado}")
            indice+=1
        else:
            print(f"[{indice}] {cementerio.getIglesia().getReligioso()} {auxEmpleado}")
            indice+=1
		
	
    indice = int(input("Ingrese el índice para escoger al religioso: "))
	
    #Validación
    while indice < 1 or indice > len(empleados):
        indice = int(input("El índice ingresado está fuera de rango. Ingrese nuevamente un índice: "))

    print()
	
    print("Dados los datos se organizará como estarán distribuidos los familiares en la Iglesia")
    print(nuevoCementerio.organizarIglesia(cliente))

    """
        


           



"""
    # Buscar cliente
    print("[1] Buscar cliente por su CC")
    print("[2] Buscar cliente por cementerio")

    #Indice cliente
    indiceCliente = int(input("Ingrese el índice correspondiente: "))
    while(indiceCliente<1 or indiceCliente>2):
        indiceCliente=int(input(("El índice ingresado está fuera de rango. Ingrese nuevamente un índice: ")))

    if indiceCliente==1:
        while cliente is None:
            cc = int(input("Ingrese CC del cliente: "))
            # Busca al cliente en todas funerarias
            prueba = Establecimiento("Establecimiento", None)
            cliente = prueba.buscarClientePorCC(cc)
            
             # Opción en caso de no estar registrado
            if cliente is None:
                print("El cliente no se encuentra registrado")
                # Puedes volver a solicitar el CC si lo necesitas

            else:
                print("Cliente Registrado:",cliente)
                if cliente.getInventario() is None:
                    print("El cliente está registrado pero no es apto para la exhumación")
                    cliente = None
                else:
                    funeraria = cliente.getInventario().getCementerio().getFuneraria()
            

    else:
        # Se escoge la funeraria con la que se va a realizar el procedimiento
        funerarias = Establecimiento.filtrarEstablecimiento("funeraria")
        print()
        print("Seleccione la funeraria correspondiente")
        indice = 0
        for auxFuneraria in funerarias:
            indice += 1
            print(f"[{indice}] {auxFuneraria}")

        indiceFuneraria = int(input("Ingrese el índice correspondiente: "))

        # Se valida que se ingrese un índice adecuado para continuar el proceso
        while indiceFuneraria < 1 or indiceFuneraria > len(funerarias):
            indiceFuneraria = int(input("El índice ingresado está fuera de rango. Ingrese nuevamente un índice: "))

        # Se realiza especialización de tipos (Establecimiento - clase padre a Funeraria - clase hija) y se asigna la funeraria correspondiente
        funeraria = funerarias[indiceFuneraria - 1]
        print()
        print("[1] Buscar cliente en cementerios de cuerpos")
        print("[2] Buscar clientes con urna fija o tumba marcada como 'default'")

        indice = int(input("Ingrese el índice correspondiente: "))

        # Validación de índice
        while indice < 1 or indice > 2:
            indice = int(input("El índice ingresado está fuera de rango. Ingrese nuevamente un índice: "))

        if indice == 1:
            print()
            print("Clientes mayor de edad")
            # Busca en la funeraria seleccionada los cementerios de cuerpos
            clientes = funeraria.buscarClienteCementerio("cuerpos", "adulto")
    
            indice = 1
            for auxCliente in clientes:
                print(f"[{indice}] {auxCliente}")
                indice += 1
            print()
            print("Clientes menor de edad")
    
            clientesNino = funeraria.buscarClienteCementerio("cuerpos", "niño")
    
            for auxCliente in clientesNino:
                print(f"[{indice}] {auxCliente}")
                indice += 1
    
            clientes.extend(clientesNino)
    
            indice = int(input("Ingrese el índice correspondiente: "))
    
            # Validación de índice
            while indice < 1 or indice > len(clientes):
                indice = int(input("El índice ingresado está fuera de rango. Ingrese nuevamente un índice: "))
    
            cliente = clientes[indice - 1]

        else:
            print("[1] Buscar tumbas marcadas como 'default'")
            print("[2] Buscar urnas marcadas como 'default'")

            indice = int(input("Ingrese el índice correspondiente: "))

            # Validación de índice
            while indice < 1 or indice > 2:
                indice = int(input("El índice ingresado está fuera de rango. Ingrese nuevamente un índice: "))

            # Se traen todos los cementerios por funeraria
            cementeriosPorFuneraria = Establecimiento.buscarPorFuneraria(funeraria, "cementerio")

            tipo = None
            mensaje1 = None
            mensaje2 = None

            if indice == 1:
                tipo = "cuerpos"
                mensaje1 = "Cementerios de cuerpos"
                mensaje2 = "Tumbas"
            elif indice == 2:
                tipo = "cenizas"
                mensaje1 = "Cementerios de cenizas"
                mensaje2 = "Urnas"
            
            # Se traen todos los cementerios de la funeraria con el atributo de tipo correspondiente ("cuerpos" o "cenizas")
            cementerios = Cementerio.cementerioPorTipo(cementeriosPorFuneraria, tipo)


            print(mensaje1)
            indice = 1
            for auxCementerio in cementerios:
            # Se muestran los cementerios correspondientes y se busca la cantidad que se encuentra en la lista de inventario que tiene como valor "default" en su atributo nombre
                cantidadDefault = len((auxCementerio).inventarioDefault())
                print(f"[{indice}] {auxCementerio} - Cantidad de {mensaje2} marcadas como default: {cantidadDefault}")
                indice += 1

            indice = int(input("Ingrese el índice correspondiente: "))

            # Validación de índice
            while indice < 1 or indice > len(cementerios):
                indice = int(input("El índice ingresado está fuera de rango. Ingrese nuevamente un índice: "))

            # Asignación de cementerio escogido
            cementerio = cementerios[indice - 1]
            print(f"{mensaje2} marcadas como default")

            # Búsqueda de inventario que tenga como valor "default" en su atributo nombre
            inventarioDefault = cementerio.inventarioDefault()

            indice = 1
            for auxTumbaUrna in inventarioDefault:
                print(f"[{indice}] {mensaje2} marcadas como {auxTumbaUrna} - Cliente: {auxTumbaUrna.getCliente()}")
                indice += 1

            indice = int(input("Ingrese el índice correspondiente: "))

            #    Validación de índice
            while indice < 1 or indice > len(inventarioDefault):
                indice = int(input("El índice ingresado está fuera de rango. Ingrese nuevamente un índice: "))

            # Asignación del cliente
            cliente = inventarioDefault[indice - 1].getCliente()
            print(f"Cliente seleccionado: {cliente} desde cementerio {tipo}: {cementerio} ")


    #Se asigna el objeto de tipo Urna o Tumba que tenga agregado el cliente
    urnaTumba=cliente.getInventario()
    #Asignar cementerio
    cementerio=cliente.getInventario().getCementerio()
    # Proceso de exhumación del cuerpo

    # Datos para la exhumación
    pesoEstatura = 0.0
    edad = 0
    tipo1 = None
    tipo2 = None

    # Iglesias disponibles
    iglesias = []

    print()
    print(f"Opciones para la exhumación del cuerpo del cliente {cliente.getNombre()}")

    maxOpcion = 1
    print("[1] Trasladar al cliente a una Urna fija en otro cementerio de cenizas")
    mensaje = "Urna"

    # Si el cliente tiene agregado un objeto de tipo Tumba es porque está en un cementerio de cuerpos y puede ser llevado a otro,
    # pero si tiene agregado un objeto de tipo Urna no puede ser trasladado a un cementerio de cuerpos
    if isinstance(urnaTumba, Tumba):
        print("[2] Trasladar al cliente a una Tumba en otro cementerio de cuerpos")
        mensaje = "Tumba"
        maxOpcion = 2

    indice = int(input("Ingrese el índice correspondiente: "))

    # Validación de índice
    while indice < 1 or indice > maxOpcion:
        indice = int(input("El índice ingresado está fuera de rango. Ingrese nuevamente un índice: "))

    if indice == 1:
        pesoEstatura = float(input("Ingrese el peso del cliente: "))
        tipo1 = "cenizas"
        tipo2 = "urna"

        # Establecer iglesia para determinar religión del cliente 
        print("Seleccione la religión con la que se va a realizar la ceremonia del cliente")
        indice = 1
        max_opcion = 0
        iglesias = []
        for auxIglesia in Iglesia:
            # Se imprimen y añaden a la lista solo las iglesias que permiten la cremación como acto final de la vida
            if auxIglesia.getCremacion():
                iglesias.append(auxIglesia)
                print(f"[{indice}] {auxIglesia.name}")
                indice += 1
                max_opcion += 1

    elif indice == 2:
        pesoEstatura = float(input("Ingrese la estatura del cliente: "))
        tipo1 = "cuerpos"
        tipo2 = "tumba"

        # Establecer iglesia para determinar religión del cliente 
        print("Seleccione la religión con la que se va a realizar la ceremonia del cliente")
        indice = 1
        max_opcion = 0
        iglesias = []
        for auxIglesia in Iglesia:
            print(f"[{indice}] {auxIglesia.name}")
            iglesias.append(auxIglesia)
            indice += 1
            max_opcion += 1

    # Fin del switch principal

    print("Indique el índice de la religión escogida: ")
    indice = int(input())

    # Validación del índice
    while indice < 1 or indice > max_opcion:
        print("El índice ingresado está fuera de rango. Ingrese nuevamente un índice: ")
        indice = int(input())

    cementerio.setIglesia(iglesias[indice - 1])
    #############################################################
    print(f"Iglesia seleccionada: {(cementerio.getIglesia()).name}")
#########################################################################
    edad = cliente.getEdad()

    print(f"La afiliación del cliente es {cliente.getAfiliacion()} se buscarán cementerios {cliente.getAfiliacion()} para su traslado")

    # Busco los cementerios del tipo solicitado en la funeraria que cumplan con las restricciones solicitadas 
    cementeriosPorTipo = cementerio.getFuneraria().buscarCementerios(tipo1, cliente)
    
    # Elimino el cementerio en el que actualmente está el cliente
    try:
        cementeriosPorTipo.remove(cementerio)
    except:
        pass

    cementerios = []

    for auxCementerio in cementeriosPorTipo:
        auxCementerio2 = auxCementerio
        auxCementerio.setIglesia(iglesias[indice - 1])
        if len(auxCementerio2.disponibilidadInventario(tipo2, pesoEstatura, edad)) != 0:
            cementerios.append(auxCementerio2)

    print()

    if len(cementerios) == 0:
        print("No se encontró inventario disponible")
        print("Se deberá añadir inventario tipo default")
        for auxCementerio in cementeriosPorTipo:
            if tipo1 == "cenizas":
                auxCementerio.agregarInventario(Urna("default", auxCementerio, pesoEstatura, edad, "fija"))

            else:
                auxCementerio.agregarInventario(Tumba("default", auxCementerio, pesoEstatura, edad))
            cementerios.append(auxCementerio)

    # print("cementerios: ", cementerios)

    indice = 1
    for auxCementerio in cementerios:
        auxCementerio2 = auxCementerio
        print(f"[{indice}] {auxCementerio2} Inventario disponible: ({len(auxCementerio2.disponibilidadInventario(tipo2, pesoEstatura, edad))})")
        indice += 1

    
    indice = int(input("Ingrese el indice del cementerio: "))

    while indice < 1 or indice > len(cementerios):
        indice = int(input("El índice ingresado está fuera de rango. Ingrese nuevamente un índice: "))

    # Eliminar cliente
    cementerio.getClientes().remove(cliente)

    # Obtener nuevo cementerio
    nuevoCementerio = cementerios[indice - 1]

    # Escoger opción más adecuada para cliente en cuánto a tamaño de la tumba comparado con estatura del cliente
    print(f"[1] Opción más adecuada en cuanto a tamaño: {nuevoCementerio.inventarioRecomendado(nuevoCementerio.disponibilidadInventario(tipo2, pesoEstatura, edad))}")
    print("[2] Buscar entre las otras opciones")

    # Ingreso del índice
    indice = int(input("Ingrese el índice correspondiente: "))

    # Validación de índice
    while indice < 1 or indice > 2:
        indice = int(input("El índice ingresado está fuera de rango. Ingrese nuevamente un índice: "))

    # Selección basada en el índice
    if indice == 1:
        nuevaUrnaTumba = nuevoCementerio.inventarioRecomendado(nuevoCementerio.disponibilidadInventario(tipo2, pesoEstatura, edad))
    elif indice == 2:
        disponible = nuevoCementerio.disponibilidadInventario(tipo2, pesoEstatura, edad)
        recomendacion = nuevoCementerio.inventarioRecomendado(nuevoCementerio.disponibilidadInventario(tipo2, pesoEstatura, edad))
        disponible.remove(recomendacion)
    
        # Imprimir opciones disponibles
        for i, auxInventario in enumerate(disponible, start=1):
            print(f"[{i}] {auxInventario}")
    
        # Ingreso del índice para la opción 2
        indice = int(input("Ingrese el índice correspondiente: "))
    
        # Validación de índice
        while indice < 1 or indice > len(disponible):
            indice = int(input("El índice ingresado está fuera de rango. Ingrese nuevamente un índice: "))
    
        nuevaUrnaTumba = disponible[indice - 1]

    #Asignacion de tumba
    nuevaUrnaTumba.agregarCliente(cliente)
	
    print(f"Se realizó correctamente el cambio al cementerio {nuevoCementerio}")
    urnaTumba.setCliente(None)

    nuevoCementerio.generarHoras()

    indice = 1
    for hora in nuevoCementerio.getHorarioEventos():
        indicador = "Pm" if int(hora[:2]) >= 12 else "Am"
        horaFormateada = hora  # Formato 12-horas con AM/PM
        print(f"[{indice}] {horaFormateada} {indicador}")
        indice += 1

    # Solicitar al usuario que ingrese el índice
    indice = int(input("Ingrese el índice para escoger el horario: "))

    #Se cambia el horario de crematorio
    nuevoCementerio.setHoraEvento(nuevoCementerio.getHorarioEventos()[indice-1])
    #Se elimina el horario de Horario eventos
    nuevoCementerio.eliminarHorario(nuevoCementerio.getHorarioEventos()[indice-1])

	#Seleccionar sepulturero
	
    print()
    print("Se inciará con el proceso de selección de empleados")
		
    print()
    print("Seleccione el empleado sepulturero disponible")

    print("Empleados disponibles en la jornada seleccionada")
    empleados =funeraria.buscarEmpleadosPorHoras(nuevoCementerio.getHoraEvento(), "sepulturero")
    indice = 1
    for auxEmpleado in empleados:
        print(f"[{indice}] {auxEmpleado}")
        indice += 1

    # Solicitar al usuario que ingrese el índice del empleado deseado
    indice = int(input("Ingrese el índice del empleado deseado: "))
    nuevoCementerio.setEmpleado(empleados[indice-1])

    print()
    print("Seleccione el empleado forense disponible")

    print("Empleados disponibles en la jornada seleccionada")
    empleados =funeraria.buscarEmpleadosPorHoras(nuevoCementerio.getHoraEvento(), "forense")
    indice = 1
    for auxEmpleado in empleados:
        print(f"[{indice}] {auxEmpleado}")
        indice += 1

    # Solicitar al usuario que ingrese el índice del empleado deseado
    indice = int(input("Ingrese el índice del empleado deseado: "))
    nuevoCementerio.setEmpleado(empleados[indice-1])
	
    #Seleccionar al padre u obispo 
    categoria=cliente.getInventario().getCategoria()
    empleado=None
    if(categoria==0):
        empleado="obispo"
    else: 
        empleado="padre"
	
    print(f"Dada la categoria [{categoria}] su ceremonia puede ser celebrada por los siguientes religiosos")
	
    empleados = cementerio.getFuneraria().buscarEmpleadosPorHoras(nuevoCementerio.getIglesia().duracionEvento(nuevoCementerio.getHoraEvento()), empleado)
 
    indice=1
    for auxEmpleado in empleados:
        if(categoria==0):
            print(f"[{indice}] {cementerio.getIglesia().getReligiosoAltoRango()} {auxEmpleado}")
            indice+=1
        else:
            print(f"[{indice}] {cementerio.getIglesia().getReligioso()} {auxEmpleado}")
            indice+=1
		
	
    indice = int(input("Ingrese el índice para escoger al religioso: "))
	
    #Validación
    while indice < 1 or indice > len(empleados):
        indice = int(input("El índice ingresado está fuera de rango. Ingrese nuevamente un índice: "))

    print()
	
    print("Dados los datos se organizará como estarán distribuidos los familiares en la Iglesia")
    print(nuevoCementerio.organizarIglesia(cliente))

    """