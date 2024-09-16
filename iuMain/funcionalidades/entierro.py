from gestorAplicacion.establecimientos.establecimiento import Establecimiento

from gestorAplicacion.establecimientos.iglesia import Iglesia
from gestorAplicacion.inventario.inventario import Inventario
from gestorAplicacion.inventario.tumba import Tumba

from gestorAplicacion.inventario.producto import Producto
import tkinter as tk

from iuMain.frame import frame1
from iuMain.frame import tablas
from iuMain.frame import FieldFrame
from iuMain.manejoErrores.errorAplicacion import errorNumeros
from iuMain.manejoErrores.errorAplicacion import errorEstatura

def titulo(frame,titulo):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text=titulo, bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

def funcionalidadEntierro(frame):

    titulo(frame,"Servicio de Cremación")

    funerarias= Establecimiento.filtrarEstablecimiento("funeraria")
    listaCliente=["Mayor de edad","Menor de edad"]
    iglesias = []
    iglesiasReligion=[]
    for auxIglesia in Iglesia:
            iglesias.append(auxIglesia)
            iglesiasReligion.append(auxIglesia.name)
            
    
    datosCliente=frame1(frame,["Funeraria","Cliente","Religión cliente"],[funerarias,listaCliente,iglesiasReligion])

    def organizacion():
         if datosCliente.continuar():
              funeraria=funerarias[datosCliente.getValores()[0]]
              #Indice cliente, si indice == 0 -> Mayor de edad, si índice == 1 -> Menor de edad
              indiceCliente=datosCliente.getValores()[1]
              iglesia=iglesias[datosCliente.getValores()[2]]
              seleccionCliente(frame,funeraria,indiceCliente,iglesia)


    btnContinuar= tk.Button(frame,text="Continuar", command=lambda:organizacion())
    btnContinuar.pack(side="top",pady=10)

def seleccionCliente(frame,funeraria,indiceCliente,iglesia):
    titulo(frame,"Datos Cliente")

    clientes=[]
    if int(indiceCliente)==0:
        clientes=funeraria.buscarCliente("adulto")
        datoCliente=frame1(frame,["Cliente"],[clientes])      
    else:
        tk.Label(frame,text="Se buscarán los clientes menores de edad a través de su Familiar Responsable").pack(pady=5)
        responsables=[]
        parentescos=[]
        IDs=[]
        id=0
        clientes=funeraria.buscarCliente("niño")
        for auxCliente in clientes:
            familiar=auxCliente.designarFamiliar(auxCliente.getFamiliares())
            responsables.append(familiar.getNombre())
            parentescos.append(familiar.getParentesco())
            IDs.append(id)
            id+=1
        
        tablas(frame,["Cliente","Familiar","Parentesco","IDs"],[clientes,responsables,parentescos,IDs])
        datoCliente=frame1(frame,["ID Cliente"],[IDs]) 

        #Frame separador 
        tk.Frame(frame).pack(pady=3)

    datoEstatura=FieldFrame(frame,[],["Ingrese la estatura del cliente"])

    def confirmacion(datoCementerio,cementerios,estatura,cliente):
        if datoCementerio.continuar():
            cementerio=cementerios[datoCementerio.getValores()[0]]
            cantidad=len(cementerio.disponibilidadInventario("tumba", estatura, cliente.getEdad()))
            cementerio.setIglesia(iglesia)
            respuesta = tk.messagebox.askyesno("Inventario disponible",f"El cementerio {cementerio} tiene ({cantidad})Tumbas disponibles \n desea continuar?")
            if respuesta:
                organizacionCementerio(frame,cliente,cementerio,estatura)
            else:
                pass
            
    def organizacion():
        if datoCliente.continuar() and datoEstatura.continuar():
            cliente=clientes[datoCliente.getValores()[0]]
            num=0
            try:
                float(datoEstatura.getValores()[0])
                estatura=float(datoEstatura.getValores()[0])
                if estatura>2 or estatura <0:
                    errorEstatura(estatura,2)
                num=1
            except:
                errorEstatura((datoEstatura.getValores()[0]),2)
                datoEstatura.borrar()
            if num==1:
                datoCliente.bloquearOpciones()
                datoEstatura.bloquear()
                btnContinuar.destroy()

                cementerios = funeraria.gestionEntierro(cliente, iglesia,estatura)
                datoCementerio=frame1(frame,["Cementerios con tumbas disponibles:"],[cementerios])

                btnContinuar1= tk.Button(frame,text="Continuar", command=lambda:confirmacion(datoCementerio,cementerios,estatura,cliente))
                btnContinuar1.pack(side="top",pady=10)
                

            

    btnContinuar= tk.Button(frame,text="Continuar", command=lambda:organizacion())
    btnContinuar.pack(side="top",pady=10)


def organizacionCementerio(frame,cliente,cementerio,estatura):
    titulo(frame,"Organizacion cementerio")

    tk.Label(frame,text="A continuación encontrará la invitación y resumen de su evento de Entierro").pack(pady=5)
    productoCementerio= Producto()
    productoCementerio.setEstablecimiento(cementerio)
    #Invitación para Entierro
    producto=productoCementerio.evento(cliente)
    print(producto)
    frameApoyo = tk.Frame(frame, bg="#772d2d")
    frameApoyo.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    invitacion = tk.Label(frameApoyo, text=producto,font=("Comic Sans MS", 14, "italic"), bg="white")
    invitacion.pack(pady=50)

    def agregarTumba(datoTumba,inventarioDisponible):
        if datoTumba.continuar():
            tumba=inventarioDisponible[datoTumba.getValores()[0]]
            tumba.agregarCliente(cliente)
            factura(frame,cliente)

    def organizacionTumba():
        titulo(frame,"Organización Tumba")
        inventarioDisponible=cementerio.disponibilidadInventario("tumba", estatura, cliente.getEdad())
        IDs = [a for a in range(len(inventarioDisponible))]
        print(IDs)
        tablas(frame,["Tumba","ID"],[inventarioDisponible,IDs])
        datoTumba=frame1(frame,["Seleccione el ID de la tumba:"],[IDs])
        btnContinuar1= tk.Button(frame,text="Continuar", command=lambda:agregarTumba(datoTumba,inventarioDisponible))
        btnContinuar1.pack(side="top",pady=10)
    
    btnContinuar= tk.Button(frameApoyo,text="Continuar", command=lambda:organizacionTumba())
    btnContinuar.pack(side="top",pady=10)

def factura(frame,cliente):

    titulo(frame,"Detalle final")
    tk.Label(frame,text="Resumen de los datos de entierro").pack(pady=5)
    tk.Label(frame,text="Se generó la siguiente factura:").pack(pady=5)

    # Frame principal
    
    # Frame de Título
    tituloFrame = tk.Frame(frame, bg="#4a90e2")
    tituloFrame.pack(fill=tk.X, pady=(0, 10))
    
    tk.Label(tituloFrame, text="FACTURA", font=("Arial", 24), bg="#4a90e2", fg="white").pack(pady=10)
    
    # Frame de Contenido
    contenido = tk.Frame(frame, bg="#ffffff", bd=1, relief=tk.SOLID)
    contenido.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    
    # Contenido del Frame
    tk.Label(contenido, text=cliente.pagoInmediato("flores"), font=("Arial", 16), bg="#ffffff").pack(pady=5)

    from iuMain.ventanaPrincipal import framePrincipal
    boton_regresar = tk.Button(contenido, text="Regresar", command=lambda: framePrincipal(frame))
    boton_regresar.pack()

   





    


    


        


