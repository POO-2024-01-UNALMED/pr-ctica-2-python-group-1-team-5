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

# Se usa para borrar lo que hay en el frame y mostrar el titulo de la funcionalidad
def titulo(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text="Servicio Cremación", bg="white", font=("Helvetica", 16, "bold"))
    titulo.pack(pady=20)

def funcionalidadCrematorio(frame):

    titulo(frame)

    #Cliente
    cliente=None
    crematorio=None

    funerarias= Establecimiento.filtrarEstablecimiento("funeraria")
    print("Seleccione la funeraria correspondiente")
    indice = 0
    for auxFuneraria in funerarias:
        indice += 1
        print(f"[{indice}] {auxFuneraria}")
    #Se escoge a la funeraria deseada
    indiceFuneraria = int(input("Ingrese el índice correspondi1ente: "))

    #Definir la funeraria
    funeraria=funerarias[indiceFuneraria-1]

    #Escoger al cliente

    print("[1] Buscar cliente mayor de edad")
    print("[2] Buscar cliente menor de edad")    
    #Indice cliente
    indiceCliente = int(input("Ingrese el índice correspondiente: "))
    listaCliente=["Mayor de edad","Menor de edad"]
##########################################################################################################
    valores = (frame1(frame,["Funeraria: ","Cliente: "],[funerarias,listaCliente])) #.valoresIndices()
##########################################################################################################
    #funeraria= funerarias[valores[0]]
    #indiceCliente = valores[1]
    
    if indiceCliente == 1:
        print("[1] Buscar cliente por su CC")
        print("[2] Buscar cliente por funeraria") 
        #Indice cliente
        indiceCliente = int(input("Ingrese el índice correspondiente: "))
        if indiceCliente==1:
            idCliente = input("Ingrese el CC del cliente: ")
            cliente = funeraria.buscarClientePorId(idCliente)
            # Validar CC correcto
            while cliente is None:
                idCliente = input("Número de CC incorrecto. Vuelve a ingresar CC del cliente: ")
                cliente = funeraria.buscarClientePorId(idCliente)
        elif indiceCliente==2:
            indice=1
            for auxCliente in funeraria.buscarCliente("adulto"):
                print("["+str(indice)+"] "+str(auxCliente))
                indice+=1
            indice=int(input("Ingrese el índice del cliente: "))
            cliente= funeraria.buscarCliente("adulto")[indice-1]

    elif indiceCliente == 2:
        indice=1
        for auxCliente in funeraria.buscarCliente("niño"):
            print("["+str(indice)+"] "+str(auxCliente))
            indice+=1
        indice=int(input("Ingrese el índice del cliente: "))   
        cliente= funeraria.buscarCliente("niño")[indice-1]
    #Cliente establecido
    print("Cliente seleccionado: "+str(cliente))

    # Buscar crematorios que coincidan con la capacidad de acompañantes del cliente y con la afiliación del cliente
    crematorios = funeraria.buscarEstablecimientos("crematorio", cliente)

    if len(crematorios) != 0:
        print(f"Su afiliación es de tipo {cliente.getAfiliacion()}")
        print(f"Los crematorios disponibles para la afiliación {cliente.getAfiliacion()} son:")

        indice=1
        for auxCrematorio in crematorios:
            print(f"[{indice}] {auxCrematorio}")
            indice+=1

    
        indice = int(input("Ingrese el índice del crematorio deseado: "))
        # Asignación de crematorio
        crematorio=crematorios[indice-1]
        
    print("Crematorio seleccionado: "+str(crematorio))

    print("Horarios disponibles del crematorio:")

    crematorio.generarHoras()

    indice = 1
    for hora in crematorio.getHorarioEventos():
        indicador = "Pm" if int(hora[:2]) >= 12 else "Am"
        horaFormateada = hora  # Formato 12-horas con AM/PM
        print(f"[{indice}] {horaFormateada} {indicador}")
        indice += 1

    # Solicitar al usuario que ingrese el índice
    indice = int(input("Ingrese el índice para escoger el horario: "))

    #Se cambia el horario de crematorio
    crematorio.setHoraEvento(crematorio.getHorarioEventos()[indice-1])
    #Se elimina el horario de Horario eventos
    crematorio.eliminarHorario(crematorio.getHorarioEventos()[indice-1])
        
    print("Empleados disponibles en la jornada seleccionada")
    empleados =funeraria.buscarEmpleadosPorHoras(crematorio.getHoraEvento(), "cremador")
    indice = 1
    for auxEmpleado in empleados:
        print(f"[{indice}] {auxEmpleado}")
        indice += 1

    # Solicitar al usuario que ingrese el índice del empleado deseado
    indice = int(input("Ingrese el índice del empleado deseado: "))
    crematorio.setEmpleado(empleados[indice-1])

    print("Seleccione la religión con la que se va a realizar la ceremonia del cliente")
    
    # Iglesias disponibles
    iglesias = []
    indice = 1

    for auxIglesia in Iglesia:
        # Se imprimen y añaden a la lista solo las iglesias que permiten la cremación como acto final de la vida
        if auxIglesia.getCremacion():
            iglesias.append(auxIglesia)
            print(f"[{indice}] {auxIglesia.name}")
            indice += 1

    indice = int(input("Indique el índice de la religión escogida: "))


    iglesia=iglesias[indice-1]
				
	#Se asigna la iglesia en el atributo iglesia en el crematorio designado para trabajar con este atributo el resto de la funcionalidad
    crematorio.setIglesia(iglesia)
				
	#se crea el productoCrematorio para guardar registro de lo que se debe cobrar en la clase Factura respecto a crematorio 
    productoCrematorio= Producto()
    productoCrematorio.setEstablecimiento(crematorio)
	#Se guardarán todos los productos que se empleen para organizar las facturas
	#productos.add(productoCrematorio);
				
	#Se imprimirá la invitación del evento
    print(productoCrematorio.evento(cliente))


    # Definir el cementerio, de acuerdo a la hora fin del evento de cremación, afiliación del cliente y el cementerio debe tener como atributo tipo el valor "cenizas"
    cementerios = funeraria.buscarCementerios("cenizas", cliente)
    # Se establecen los horarios del cementerio de acuerdo a la finalización de ceremonia de cremación
    crematorio.cambiarHorarios(cementerios)

    indice = 1
    # Se imprimen los cementerios
    print("Cementerios disponibles")

    for auxCementerio in cementerios:
        print(f"[{indice}] {auxCementerio} - Horarios disponibles {len(auxCementerio.getHorarioEventos())}")
        indice += 1

    indice = int(input("Indique el índice del cementerio: "))

    # Se agrega el cementerio seleccionado
    cementerio = cementerios[indice - 1]
    # Se añade la iglesia seleccionada al cementerio
    cementerio.setIglesia(iglesia)

    # Escoger horario para el cementerio

    indice = 1
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
    print("Material seleccionado:", urna.getMaterialSeleccionado())