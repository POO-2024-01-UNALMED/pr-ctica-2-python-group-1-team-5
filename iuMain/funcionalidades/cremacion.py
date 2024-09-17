#Autores 
# Violeta Gomez


from gestorAplicacion.establecimientos.establecimiento import Establecimiento
from gestorAplicacion.establecimientos.iglesia import Iglesia
from gestorAplicacion.inventario.inventario import Inventario
from gestorAplicacion.inventario.urna import Urna

from gestorAplicacion.inventario.producto import Producto
import tkinter as tk

from iuMain.frame import frame1
from iuMain.frame import tablas
from iuMain.frame import FieldFrame
from iuMain.manejoErrores.errorAplicacion import errorIds
from iuMain.manejoErrores.errorAplicacion import errorPeso

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
            if valorCliente.continuar(etiquetaCliente[0]):
               
                
                cliente=listaClientes[(valorCliente.getValores())[0]]
               
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
        tk.Label(frame,text="Se debe seleccionar el crematorio y la iglesia por la que se quiere realizar la ceremonia").pack(pady=5)
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
            valMinIglesia=1
            if valoresCrematorio.continuar() and valorIglesia.continuar():
                crematorio=crematorios[(valoresCrematorio.getValores())[0]]
               

                def cambiarHoras(horas):
                    if horas.continuar():
                        horaEscogida=crematorio.getHorarioEventos()[(horas.getValores())[0]]
                        crematorio.setHoraEvento(horaEscogida)
                        crematorio.setIglesia(iglesia)
                        ventanaHoras.destroy()
                        cementerios(frame,crematorio,iglesia,cliente)
              
                try:
                    valMin=1
                    iglesia=iglesias[int(valorIglesia.getValores()[0])-1]
                    if int(valorIglesia.getValores()[0])<valMin:
                        raise errorIds(iglesias[int(valorIglesia.getValores()[0])],"El ID ingresado es incorrecto",1)
                    #Crear ventana para determinar la hora del crematorio
                    ventanaHoras = tk.Toplevel()
                    ventanaHoras.title("Funeraria Rosario")
                    ventanaHoras.geometry("400x200")
                    label = tk.Label(ventanaHoras, text=f"Crematorio {crematorio.getNombre()}", padx=10, anchor="w", wraplength=480)
                    label.pack(pady=2)
                    crematorio.generarHoras()
                    
                    horarios = crematorio.getHorarioEventos()
                   
                    horasGenereadas= lambda horarios: [f"{hora} {'Pm' if int(hora[:2]) >= 12 else 'Am'}"for i, hora in enumerate(horarios)]
                    horariosFormateados = horasGenereadas(horarios)
                  
                    horas = frame1(ventanaHoras,[f"Horarios disponibles:"],[horariosFormateados])
                  
                    btnContinuar = tk.Button(ventanaHoras, text="Continuar",command=lambda: cambiarHoras(horas))
                    btnContinuar.pack(pady=20)

                    ventanaHoras.mainloop()    
                    
                except:
                    errorIds(valorIglesia.getValores()[0],"El ID ingresado no es correcto",valMin)
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
         
            empleado=empleados[(valores.getValores())[0]]
          

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
         
                horarios = cementerio.getHorarioEventos()
             
                horasGenereadas= lambda horarios: [f"{hora} {'Pm' if int(hora[:2]) >= 12 else 'Am'}"for i, hora in enumerate(horarios)]
                horariosFormateados = horasGenereadas(horarios)
              
                horas = frame1(ventanaHoras,[f"Horarios disponibles:"],[horariosFormateados])
                
               
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
    valoresUrna=FieldFrame(frame,[],["Categoria urna (0-2)","Peso cliente (0-120)kg"],[0,0])
    

    
    num=0
    def validarUrnas(valoresUrna):
        num=0
        if valoresUrna.continuar():
            categoria =(valoresUrna.getValores()[0])
            
            peso = (valoresUrna.getValores()[1])

            try:
                int(categoria)
                if int(categoria)<0 or int(categoria)>2:
                    raise errorIds(int(categoria),"La categoria ingresada no es correcta",0,2)
            except ValueError:
                raise errorIds(categoria,"La categoria ingresada no es correcta",0,2)
            try:
                float(peso)
                if float(peso)>120 or float(peso)<0:
                    raise errorPeso(peso,120)
                num=1
            except ValueError:
                raise errorPeso(peso,120)
        if num==1:
            valoresUrna.bloquear()
            btnContinuar.destroy()
            tablaUrnas(frame,cementerio,crematorio,cliente,valores,categoria,peso)
    
    btnContinuar= tk.Button(frame,text="Continuar", command=lambda: validarUrnas(valoresUrna))
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
        IDs=list(p for p in range(0,len(urnas)))
        tablas(frame,["Urnita","Cementerio","Tipo","ID"],[urnas,cementerios,tipos,IDs])

        entradaUrna=FieldFrame(frame,[],["Indique el ID de la Urna"])

    def datosCrematorio():

        if entradaUrna.continuar():
            num=0
            try:
                urna=urnas[int(entradaUrna.getValores()[0])]  
                if int(entradaUrna.getValores()[0])<0:
                    raise errorIds(urnas[int(entradaUrna.getValores()[0])],"El ID ingresado es incorrecto",0)
               
                num=1
            except:
                errorIds(entradaUrna.getValores()[0],"El ID ingresado no es correcto",0,len(urnas)-1)
                entradaUrna.borrar()
            if num==1:
                tk.messagebox.showinfo("Información", f"Ha seleccionado la Urna {urna}")
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


   