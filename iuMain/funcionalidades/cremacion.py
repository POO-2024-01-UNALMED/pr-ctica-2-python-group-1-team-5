from gestorAplicacion.establecimientos.establecimiento import Establecimiento
#from gestorAplicacion.establecimientos.cementerio import Cementerio
#from gestorAplicacion.establecimientos.crematorio import Crematorio
#from gestorAplicacion.establecimientos.funeraria import Funeraria
from gestorAplicacion.establecimientos.iglesia import Iglesia

#from gestorAplicacion.financiero.banco import Banco
#from gestorAplicacion.financiero.cuentaBancaria import CuentaBancaria

#from gestorAplicacion.personas.persona import Persona
#from gestorAplicacion.personas.cliente import Cliente
#from gestorAplicacion.personas.empleado import Empleado
#from gestorAplicacion.personas.familiar import Familiar

from gestorAplicacion.inventario.inventario import Inventario
from gestorAplicacion.inventario.urna import Urna
#from gestorAplicacion.inventario.tumba import Tumba
from gestorAplicacion.inventario.producto import Producto
import tkinter as tk

from iuMain.frame import frame1
from iuMain.frame import tablas
from iuMain.frame import FieldFrame
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



def funcionalidadCrematorio(frame):

    titulo(frame,"Servicio de Cremación")

    funerarias= Establecimiento.filtrarEstablecimiento("funeraria")

    listaCliente=["Mayor de edad","Menor de edad"]
##########################################################################################################
    valores = frame1(frame,["Funeraria: ","Cliente: "],[funerarias,listaCliente])
    btnContinuar= tk.Button(frame,text="Continuar", command=lambda:seleccionCliente(frame,valores))
    btnContinuar.pack(side="top",pady=10)
##########################################################################################################
def seleccionCliente(frame,valores):
 
    if valores.continuar():
        funerarias= Establecimiento.filtrarEstablecimiento("funeraria")
        #Funeraria seleccionada
        funeraria= funerarias[(valores.getValores())[0]]
        indiceCliente =valores.getValores()[1]
        etiquetaCliente=[]

        if indiceCliente == 0:
            etiquetaCliente=["Clientes mayor de edad"]
            listaClientes=funeraria.buscarCliente("adulto")
            opcionesCliente=[listaClientes]
          
        elif indiceCliente==1:    
            etiquetaCliente=["Clientes menor de edad"]
            listaClientes=funeraria.buscarCliente("niño")
            opcionesCliente=[listaClientes]

        global current_frame,separador
        if current_frame:
            current_frame.destroy()
        if separador:
            separador.destroy()

        frameSeparador=tk.Frame(frame)
        frameSeparador.pack(pady=25)
        valorCliente = frame1(frame,etiquetaCliente,opcionesCliente)

          
        def datosCliente():
            if valorCliente.continuar():
                print(valorCliente.getValores()[0])
                print(listaClientes)
                
                cliente=listaClientes[(valorCliente.getValores())[0]]
                print(cliente.getNombre())
                texto=f"Has seleccionado al cliente {cliente} \n ¿Deseas continuar?"
                result = tk.messagebox.askyesno("Confirmar Datos",texto)
                
                if result:
                    organizacionCrematorio(frame,funeraria,cliente)
                else:
                    tk.messagebox.showinfo("", "No es posible continuar con el proceso sin asignar un Cliente")
                    current_frame.destroy()
                    separador.destroy()
                    funcionalidadCrematorio()


        btnContinuar= tk.Button(valorCliente,text="Continuar", command=lambda:datosCliente())
        btnContinuar.grid(row=1, column=2)
        
        current_frame = valorCliente
        separador=frameSeparador

    def organizacionCrematorio(frame,funeraria,cliente):

        titulo(frame,"Organizacion Crematorio")
        #texto inicial
        texto= tk.Label(frame,text=f"Los crematorios disponibles para la afiliación {cliente.getAfiliacion()} son:")
        texto.pack(side="top",pady=5)
        # Buscar crematorios que coincidan con la capacidad de acompañantes del cliente y con la afiliación del cliente
        crematorios = funeraria.buscarEstablecimientos("crematorio", cliente)
        valoresCrematorio=frame1(frame,["Crematorios"],[crematorios])
        frameSeparador=tk.Frame(frame)
        frameSeparador.pack(pady=10)
        
        # Iglesias disponibles
        iglesiasNombre = []
        iglesiasReligion=[]
        iglesias=[]


        for auxIglesia in Iglesia:
            # Se imprimen y añaden a la lista solo las iglesias que permiten la cremación como acto final de la vida
            if auxIglesia.getCremacion():
                iglesiasNombre.append(auxIglesia.getNombre())
                iglesiasReligion.append(auxIglesia.name)
                iglesias.append(auxIglesia)

        texto= tk.Label(frame,text="Iglesias disponibles: ")
        texto.pack(side="top",pady=5)
        valoresFilasColumnas= tablas(frame,["Religión","Nombre Iglesia","ID"],[iglesiasReligion,iglesiasNombre,list(map(lambda x: x, range(1, len(iglesiasNombre)+1)))])
        
        valorIglesia=FieldFrame(frame,[],["Indique el ID de la iglesia"])


        def datosCrematorio():

            if valoresCrematorio.continuar() and valorIglesia.continuar():
                crematorio=crematorios[(valoresCrematorio.getValores())[0]]
                print(crematorio)
                print(int(valorIglesia.getValores()[0])-1)
                print(iglesias)

                def cambiarHoras(horas):
                    if horas.continuar():
                        horaEscogida=crematorio.getHorarioEventos()[(horas.getValores())[0]]
                        crematorio.setHoraEvento(horaEscogida)
                        crematorio.setIglesia(iglesia)
                        ventanaHoras.destroy()
                        cementerios(frame,crematorio,iglesia,cliente)
                try:
                    iglesia=iglesias[int(valorIglesia.getValores()[0])-1]
                    #Crear ventana para determinar la hora del crematorio
                    ventanaHoras = tk.Toplevel()
                    ventanaHoras.title("Funeraria Rosario")
                    ventanaHoras.geometry("400x200")
                    label = tk.Label(ventanaHoras, text=f"Crematorio {crematorio.getNombre()}", padx=10, anchor="w", wraplength=480)
                    label.pack(pady=2)
                    crematorio.generarHoras()
                    print(crematorio.generarHoras())
                    horarios = crematorio.getHorarioEventos()
                    print(horarios)
                    horasGenereadas= lambda horarios: [f"{hora} {'Pm' if int(hora[:2]) >= 12 else 'Am'}"for i, hora in enumerate(horarios)]
                    horariosFormateados = horasGenereadas(horarios)
                    print(horariosFormateados)
                    horas = frame1(ventanaHoras,[f"Horarios disponibles:"],[horariosFormateados])
                    
                    print(horas)
                    btnContinuar = tk.Button(ventanaHoras, text="Continuar",command=lambda: cambiarHoras(horas))
                    btnContinuar.pack(pady=20)

                    ventanaHoras.mainloop()    
                    
                except:
                    errorNumeros(valorIglesia.getValores()[0],"El ID ingresado no es correcto")
                    valorIglesia.borrar()
        
        btnContinuar= tk.Button(frame,text="Continuar", command=datosCrematorio)
        btnContinuar.pack(pady=5,padx=10)
        
        

def cementerios(frame,crematorio,iglesia,cliente):
    #funeraria=None
    #crematorio=None
    #cliente=None
    titulo(frame,"Organizacion Cementerio")

    texto= tk.Label(frame,text="Seleccione los siguientes datos:")
    texto.pack(side="top",pady=5)
    
    #Empleados disponibles según la hora
    empleados =(crematorio.getFuneraria()).buscarEmpleadosPorHoras(crematorio.getHoraEvento(), "cremador")
    # Definir el cementerio, de acuerdo a la hora fin del evento de cremación, afiliación del cliente y el cementerio debe tener como atributo tipo el valor "cenizas"
    cementerios = (crematorio.getFuneraria()).buscarCementerios("cenizas", cliente)
    # Se establecen los horarios del cementerio de acuerdo a la finalización de ceremonia de cremación
    crematorio.cambiarHorarios(cementerios)

    valores= frame1(frame,["Empleados:","Cementerios cenizas"],[empleados,cementerios])

    def datosCementerio(valores):

        if valores.continuar():
    
            cementerio=cementerios[(valores.getValores())[1]]
            print(cementerio.getNombre())
            empleado=empleados[(valores.getValores())[0]]
            print(empleado)

            def cambiarHoras(horas):
                if horas.continuar():
                    horaEscogida=cementerio.getHorarioEventos()[(horas.getValores())[0]]
                    cementerio.setHoraEvento(horaEscogida)
                    cementerio.setIglesia(iglesia)
                    ventanaHoras.destroy()
                    btnContinuar.destroy()
                    urnas(frame,cementerio,crematorio,cliente,valores)
                    
                
            #iglesia=iglesias[int(valorIglesia.getValores()[0])-1]
            #Crear ventana para determinar la hora del crematorio
            texto=f"El cementerio {cementerio} cuenta con {len(cementerio.getHorarioEventos())}\n ¿Deseas continuar?"
            result = tk.messagebox.askyesno("Confirmar Datos",texto)
            if result:
                ventanaHoras = tk.Toplevel()
                ventanaHoras.title("Funeraria Rosario")
                ventanaHoras.geometry("400x200")
                label = tk.Label(ventanaHoras, text=f"Cementerio {cementerio.getNombre()}", padx=10, anchor="w", wraplength=480)
                label.pack(pady=2)
                #crematorio.generarHoras()
                #print(crematorio.generarHoras())
                horarios = cementerio.getHorarioEventos()
                print(horarios)
                horasGenereadas= lambda horarios: [f"{hora} {'Pm' if int(hora[:2]) >= 12 else 'Am'}"for i, hora in enumerate(horarios)]
                horariosFormateados = horasGenereadas(horarios)
                print(horariosFormateados)
                horas = frame1(ventanaHoras,[f"Horarios disponibles:"],[horariosFormateados])
                
                print(horas)
                btnContinuar1 = tk.Button(ventanaHoras, text="Continuar",command=lambda: cambiarHoras(horas))
                btnContinuar1.pack(pady=20)

                ventanaHoras.mainloop()    
                    

    btnContinuar= tk.Button(frame,text="Continuar", command=lambda:datosCementerio(valores))
    btnContinuar.pack(side="top",pady=10)

def urnas(frame,cementerio,crematorio,cliente,valores):
    #titulo(frame,"")
    valores.bloquearOpciones()
    frameSeparador=tk.Frame(frame)
    frameSeparador.pack(pady=20)
    valoresUrna=FieldFrame(frame,["Datos Urna","Valores"],["Categoria urna (0-2)","Peso cliente (0-120)"],[0,0])
    categoria =((valoresUrna.getValores())[0])
    peso = ((valoresUrna.getValores())[1])
    num=0
    def validarUrnas():
        if valoresUrna.continuar():
            try:
                int(categoria)
                float(peso)
                num=1
            except:
                errorNumeros(categoria,"La categoria ingresada no es correcta")
                errorNumeros(peso,"El peso ingresado no es correcto")
        if num==1:
            valoresUrna.bloquear()
            btnContinuar.destroy()
            tablaUrnas(frame,cementerio,crematorio,cliente,valores,categoria,peso)
    
    btnContinuar= tk.Button(frame,text="Continuar", command=lambda: validarUrnas())
    btnContinuar.pack(side="top",pady=10)

#___________________________________________________________________________________________________________________

def tablaUrnas(frame,cementerio,crematorio,cliente,valores,categoria,peso):
    #titulo(frame,"")
    valores.bloquearOpciones()
    
    iglesia = cementerio.getIglesia()
    tiposUrnas = iglesia.getTipoUrna()
    
    etiqueta = tk.Label(frame, text="Urnas disponibles para su religión: " + ", ".join(tiposUrnas))
    etiqueta.pack(pady=5)

    urnas = cementerio.disponibilidadInventario("urna", float(peso), int(categoria))
    if not urnas:
        etiqueta1=tk.Label(frame,text="")
        etiqueta1.pack(pady=5)
        tk.messagebox.showerror("Error", "No se encontraron urnas disponibles para el cliente, \nse deberá añadir una urna default.")
        tipo = tiposUrnas[0]
        urna = Urna("default", cementerio, float(peso), int(categoria), tipo)
        producto(frame,cliente, urna, crematorio)

    else:
        cementerios= list(map(lambda p: p.getCementerio().getNombre(), urnas))
        tipos = list(map(lambda e: e.getTipo(),urnas))
        IDs=list(p for p in range(1,len(urnas)))
        tablas(frame,["Urnita","Cementerio","Tipo","ID"],[urnas,cementerios,tipos,IDs])

        entradaUrna=FieldFrame(frame,[],["Indique el ID de la Urna"])

    def datosCrematorio():

        if entradaUrna.continuar():
            num=0
            try:
                urna=urnas[int(entradaUrna.getValores()[0])-1]  
                print(urna)
                print(urnas)
                num=1
            except:
                errorNumeros(entradaUrna.getValores()[0],"El ID ingresado no es correcto")
                entradaUrna.borrar()
            if num==1:
                producto(frame,cliente,urna,crematorio)
    
    btnContinuar= tk.Button(frame,text="Continuar", command=datosCrematorio)
    btnContinuar.pack(pady=5,padx=10)


def producto(frame, cliente, urna,crematorio):
    titulo(frame,"Invitación a la ceremonia") 
    # Agregar cliente a la urna
    urna.agregarCliente(cliente)
    productoCrematorio= Producto()
    productoCrematorio.setEstablecimiento(crematorio)
   
    frameApoyo = tk.Frame(frame, bg="#772d2d")
    frameApoyo.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    invitacion = tk.Label(frameApoyo, text=productoCrematorio.evento(cliente),font=("Comic Sans MS", 14, "italic"), bg="white")
    invitacion.pack(pady=50)

    from iuMain.ventanaPrincipal import framePrincipal
    boton_regresar = tk.Button(frameApoyo, text="Regresar", command=lambda: framePrincipal(frame))
    boton_regresar.pack()

    """indice = 1
    for auxEmpleado in empleados:
        print(f"[{indice}] {auxEmpleado}")
        indice += 1

 

    # Solicitar al usuario que ingrese el índice del empleado deseado
    indice = int(input("Ingrese el índice del empleado deseado: "))
    crematorio.setEmpleado(empleados[indice-1])"""

#_________________________________________________________________________________________________
				
	#se crea el productoCrematorio para guardar registro de lo que se debe cobrar en la clase Factura respecto a crematorio 
    productoCrematorio= Producto()
    #productoCrematorio.setEstablecimiento(crematorio)
	
   # _____________________________________________________________________________________________
    
    #Se guardarán todos los productos que se empleen para organizar las facturas
	#productos.add(productoCrematorio);
				
	#Se imprimirá la invitación del evento
    #print(productoCrematorio.evento(cliente))

#_________________________________________________________________________________________________


    #indice = 1
    # Se imprimen los cementerios
    #print("Cementerios disponibles")

    #for auxCementerio in cementerios:
        #print(f"[{indice}] {auxCementerio} - Horarios disponibles {len(auxCementerio.getHorarioEventos())}")
        #indice += 1

    #indice = int(input("Indique el índice del cementerio: "))

    # Se agrega el cementerio seleccionado
    #cementerio = cementerios[indice - 1]
    # Se añade la iglesia seleccionada al cementerio
    #cementerio.setIglesia(iglesia)

    # Escoger horario para el cementerio

    """indice = 1
    for hora in cementerio.getHorarioEventos():
        indicador = "Pm" if int(hora[:2]) >= 12 else "Am"
        horaFormateada = hora  # Formato 12-horas con AM/PM
        print(f"[{indice}] {horaFormateada} {indicador}")
        indice += 1

    # Solicitar al usuario que ingrese el índice
    indice = int(input("Ingrese el índice para escoger el horario: "))

    #Se cambia el horario de crematorio
    cementerio.setHoraEvento(cementerio.getHorarioEventos()[indice-1])
    #Se elimina el horario de Horario eventos
    cementerio.eliminarHorario(cementerio.getHorarioEventos()[indice-1])


    iglesia = crematorio.getIglesia()
    tiposUrnas = iglesia.getTipoUrna()
    
    # Mostrar tipos de urnas
    print("El tipo de urnas disponibles para su religión son: ")
    for tipo in tiposUrnas:
        print(tipo)
    
    # Solicitar peso del cliente
    peso = float(input("Ingrese un número de 0 a 120 que indique el peso en kg del cliente: "))
    
    # Selección de categoría
    print("Seleccione la categoría para la urna del cliente")
    print("[0] Se puede escoger un arreglo floral")
    print("[1] Se pueden escoger tres arreglos florales")
    print("[2] Se pueden escoger tres arreglos florales y material para la Urna")
    
    while True:
        try:
            categoria = int(input("Indique el índice de la categoría deseada: "))
            if 0 <= categoria <= 2:
                break
            else:
                print("El índice ingresado está fuera de rango.")
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")
    
    # Filtrar urnas
    urnas = cementerio.disponibilidadInventario("urna", peso, categoria)
    
    urna = None
    
    if not urnas:
        print("No se encontraron urnas disponibles para el cliente, se deberá añadir una provisional")
        tipo = tiposUrnas[0]
        urna = Urna("default", cementerio, peso, categoria, tipo)
        print(f"Urna {urna} añadida")
        
        # Agregar cliente a la urna
        urna.agregarCliente(cliente)
        
    else:
        # Mostrar urnas disponibles
        print("Escoja la urna de su preferencia: ")
        for idx, auxUrna in enumerate(urnas, start=1):
            print(f"[{idx}] {auxUrna}")
        
        while True:
            try:
                indice = int(input("Indique el índice de la Urna: "))
                if 1 <= indice <= len(urnas):
                    break
                else:
                    print("El índice ingresado está fuera de rango.")
            except ValueError:
                print("Entrada inválida. Ingrese un número válido.")
        
        # Designar urna para el cliente
        urna = urnas[indice - 1]
        urna.agregarCliente(cliente)
    
    # Generar adornos
    urna.generarAdornos("flores")
    urna.generarAdornos("material")

    # Obtener el inventario de flores y materiales disponibles
    flores = Inventario.flores
    materiales = Inventario.material

    print("Seleccione las flores que adornarán la urna")

    numero = 0

    # Si la categoría es 0, solo se podrán escoger 2 flores del arreglo
    if categoria == 0:
        numero = 1
    else:
        numero = 3
        urna.setMaterialSeleccionado(None)  # Cambiar materialSeleccionado a None

    while numero > 0:
        indice = 1
        for flor in flores:
            # Contar la cantidad de cada una de las flores
            print(f"[{indice}] {flor} cantidad disponible: {urna.contarAdorno(flor, 'flores')}")
            indice += 1
        indice = int(input("Indique el índice de las flores que quiere agregar: "))


        # Agregar las flores seleccionadas y eliminarlas del inventario
        urna.agregarAdorno(flores[indice - 1], "flores")
        numero -= 1

    # Salto
    print()

    indice = 1
    if urna.getMaterialSeleccionado() is None:
        print("Indique el material de su preferencia")
        for material in materiales:
            # Contar la cantidad de cada uno de los materiales
            print(f"[{indice}] {material} cantidad disponible: {urna.contarAdorno(material, 'material')}")
            indice += 1
        indice = int(input("Indique el índice del material que quiere agregar: "))

    # Validación
    while indice < 1 or indice > len(materiales):
        indice = int(input("El índice ingresado está fuera de rango. Ingrese nuevamente un índice: "))

    # Agregar el material seleccionado y eliminarlo del inventario
    urna.agregarAdorno(materiales[indice - 1], "material")

    # Imprimir flores y material seleccionados
    print("Flores seleccionadas:", urna.getFloresSeleccionadas())
    print("Material seleccionado:", urna.getMaterialSeleccionado())"""