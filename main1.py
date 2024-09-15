from gestorAplicacion.establecimientos.establecimiento import Establecimiento
from gestorAplicacion.establecimientos.cementerio import Cementerio
from gestorAplicacion.establecimientos.crematorio import Crematorio
from gestorAplicacion.establecimientos.funeraria import Funeraria
from gestorAplicacion.establecimientos.iglesia import Iglesia

from gestorAplicacion.financiero.banco import Banco
from gestorAplicacion.financiero.cuentaBancaria import CuentaBancaria

from gestorAplicacion.personas.persona import Persona
from gestorAplicacion.personas.cliente import Cliente
from gestorAplicacion.personas.empleado import Empleado
from gestorAplicacion.personas.familiar import Familiar

from gestorAplicacion.inventario.inventario import Inventario
from gestorAplicacion.inventario.urna import Urna
from gestorAplicacion.inventario.tumba import Tumba
from gestorAplicacion.inventario.producto import Producto

from iuMain.funcionalidades import cremacion
from iuMain.funcionalidades import exhumacion
from iuMain import ventanaInicio



"""def funcionalidadCrematorio():

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
    print("Material seleccionado:", urna.getMaterialSeleccionado()) """



"""def funcionalidadExhumacion():
    cliente = None
    urnaTumba = None
    cementerio = None
    nuevaUrnaTumba = None

    print()
    # Breve descripción de la funcionalidad para los usuarios
    print("La exhumación es el proceso de retirar un cuerpo de su lugar de sepultura")
    print()

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
            print("[2] Buscar urnas marcadas como 'default']")

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
    print(nuevoCementerio.organizarIglesia(cliente))"""
		


    


    

if __name__ == "__main__":

    #Bancos
    banco1 = Banco.BBVA
    banco2 = Banco.BANCOLOMBIA
    banco3 = Banco.BANCO_OCCIDENTE
    banco4 = Banco.BANCO_BOGOTA
    banco5 = Banco.DAVIVIENDA

    #Cuentas Bancarias funerarias
    # Cuentas corrientes
    cuentaF1= CuentaBancaria(100203, "Eterna Paz",banco1, 0, 100000, 100000, 100000, 10000)
    cuentaF2= CuentaBancaria(100564, "Camino de Luz", banco2, 0, 100000, 100000, 100000, 10000)
    cuentaF3= CuentaBancaria(100233, "Recuerdos Eternos",banco3, 0, 100000, 100000, 100000, 10000)
    
    #Cuenta ahorros
    cuentaF4= CuentaBancaria(135635, "Todas",banco4, 2030203)
    
    #Funerarias
    funeraria1= Funeraria("Eterna Paz",cuentaF1,cuentaF4)
    funeraria2= Funeraria("Caminos de Luz",cuentaF2,cuentaF4)
    funeraria3= Funeraria("Recuerdos Eternos",cuentaF3,cuentaF4)


    # Empleados generales

    #Cuenta empleados conductor
    cuentaEC1 = CuentaBancaria(148689, "Bruno Salgado",banco1, 1293433)
    cuentaEC2 = CuentaBancaria(145646, "Bárbara López",banco2, 129343)
    cuentaEC3 = CuentaBancaria(123450, "Óscar Morales",banco3, 12934)
    cuentaEC4 = CuentaBancaria(406864, "Dulce María Reyes",banco4, 12933)
    cuentaEC5 = CuentaBancaria(496345, "Evelyn Rodríguez",banco5, 12933)
    cuentaEC6 = CuentaBancaria(694969, "Kevin Castillo",banco1, 1293)
   
    # Empleados conductor
    empleadoC1 = Empleado("Bruno Salgado", cuentaEC1, "mañana", "conductor", 10000, funeraria1)
    empleadoC2 = Empleado("Bárbara López", cuentaEC2, "mañana", "conductor", 10000, funeraria1)
    empleadoC3 = Empleado("Óscar Morales", cuentaEC3, "tarde", "conductor", 10000, funeraria1)
    empleadoC4 = Empleado("Dulce María Reyes", cuentaEC4, "tarde", "conductor", 10000, funeraria1)
    empleadoC5 = Empleado("Evelyn Rodríguez", cuentaEC5, "noche", "conductor", 10000, funeraria1)
    empleadoC6 = Empleado("Kevin Castillo", cuentaEC6, "noche", "conductor", 10000, funeraria1)
    
    #Cuenta empleados forense
    cuentaEF1 = CuentaBancaria(135439, "Ana García",banco1, 1293433)
    cuentaEF2 = CuentaBancaria(147788, "Luca Rossi",banco2, 129343)
    cuentaEF3 = CuentaBancaria(188867, "Ayesha Khan",banco3, 12934)
    cuentaEF4 = CuentaBancaria(445556, "Jorge Martínez",banco4, 12933)
    cuentaEF5 = CuentaBancaria(492345, "Sofia Petrov",banco5, 12933)
    cuentaEF6 = CuentaBancaria(696788, "Haruto Tanaka",banco1, 1293)
   
    # Empleados forense
    empleadoF1 = Empleado("Ana García", cuentaEF1, "mañana", "forense", 1000, funeraria1)
    empleadoF2 = Empleado("Luca Rossi", cuentaEF2, "mañana", "forense", 1000, funeraria1)
    empleadoF3 = Empleado("Ayesha Khan", cuentaEF3, "tarde", "forense", 1000, funeraria1)
    empleadoF4 = Empleado("Jorge Martínez", cuentaEF4, "tarde", "forense", 1000, funeraria1)
    empleadoF5 = Empleado("Sofia Petrov", cuentaEF5, "noche", "forense", 1000, funeraria1)
    empleadoF6 = Empleado("Haruto Tanaka", cuentaEF6, "noche", "forense", 1000, funeraria1)

    #Cuenta empleados padre
    cuentaEP1 = CuentaBancaria(675768, "Elena Inanova",banco1, 1293433)
    cuentaEP2 = CuentaBancaria(143445, "Amir Reza",banco2, 129343)
    cuentaEP3 = CuentaBancaria(187899, "Mia Eriksson",banco3, 12934)
    cuentaEP4 = CuentaBancaria(442342, "Dulce María Reyes",banco4, 12933)
    cuentaEP5 = CuentaBancaria(413244, "Nina Jovanović",banco5, 12933)
    cuentaEP6 = CuentaBancaria(697899, "Kevin Castillo",banco1, 1293)
    
    # Empleados padre
    empleadoP1 = Empleado("Elena Ivanova", cuentaEP1, "mañana", "padre", 1000, funeraria1)
    empleadoP2 = Empleado("Amir Reza", cuentaEP2, "mañana", "padre", 1000, funeraria1)
    empleadoP3 = Empleado("Mia Eriksson", cuentaEP3, "tarde", "padre", 1000, funeraria1)
    empleadoP4 = Empleado("Dulce María Reyes", cuentaEP4, "tarde", "padre", 1000, funeraria1)
    empleadoP5 = Empleado("Nina Jovanović", cuentaEP5, "noche", "padre", 1000, funeraria1)
    empleadoP6 = Empleado("Kevin Castillo", cuentaEP6, "noche", "padre", 1000, funeraria1)

    #Cuenta empleados obispo
    cuentaEO1 = CuentaBancaria(123122, "Eli Cohen",banco1, 1293433)
    cuentaEO2 = CuentaBancaria(244433, "Bárbara López",banco2, 129343)
    cuentaEO3 = CuentaBancaria(456666, "Marco Bianchi",banco3, 12934)
    cuentaEO4 = CuentaBancaria(423444, "Zara Ahmed",banco4, 12933)
    cuentaEO5 = CuentaBancaria(488707, "Evelyn Rodríguez",banco5, 12933)
    cuentaEO6 = CuentaBancaria(707070, "Raj Patel",banco1, 1293)
    
    # Empleados obispo
    empleadoO1 = Empleado("Eli Cohen", cuentaEO1, "mañana", "obispo", 1000, funeraria1)
    empleadoO2 = Empleado("Bárbara López", cuentaEO2, "mañana", "obispo", 1000, funeraria1)
    empleadoO3 = Empleado("Marco Bianchi", cuentaEO3, "tarde", "obispo", 1000, funeraria1)
    empleadoO4 = Empleado("Zara Ahmed", cuentaEO4, "tarde", "obispo", 1000, funeraria1)
    empleadoO5 = Empleado("Evelyn Rodríguez", cuentaEO5, "noche", "obispo", 1000, funeraria1)
    empleadoO6 = Empleado("Raj Patel", cuentaEO6, "noche", "obispo", 1000, funeraria1)

    # Agregar empleados a funeraria 2
    funeraria2.agregarEmpleado(empleadoC1)
    funeraria2.agregarEmpleado(empleadoC2)
    funeraria2.agregarEmpleado(empleadoC3)
    funeraria2.agregarEmpleado(empleadoC4)
    funeraria2.agregarEmpleado(empleadoC5)
    funeraria2.agregarEmpleado(empleadoC6)

    funeraria2.agregarEmpleado(empleadoF1)
    funeraria2.agregarEmpleado(empleadoF2)
    funeraria2.agregarEmpleado(empleadoF3)
    funeraria2.agregarEmpleado(empleadoF4)
    funeraria2.agregarEmpleado(empleadoF5)
    funeraria2.agregarEmpleado(empleadoF6)

    funeraria2.agregarEmpleado(empleadoP1)
    funeraria2.agregarEmpleado(empleadoP2)
    funeraria2.agregarEmpleado(empleadoP3)
    funeraria2.agregarEmpleado(empleadoP4)
    funeraria2.agregarEmpleado(empleadoP5)
    funeraria2.agregarEmpleado(empleadoP6)

    funeraria2.agregarEmpleado(empleadoO1)
    funeraria2.agregarEmpleado(empleadoO2)
    funeraria2.agregarEmpleado(empleadoO3)
    funeraria2.agregarEmpleado(empleadoO4)
    funeraria2.agregarEmpleado(empleadoO5)
    funeraria2.agregarEmpleado(empleadoO6)

    # Agregar empleados a funeraria 3
    funeraria3.agregarEmpleado(empleadoC1)
    funeraria3.agregarEmpleado(empleadoC2)
    funeraria3.agregarEmpleado(empleadoC3)
    funeraria3.agregarEmpleado(empleadoC4)
    funeraria3.agregarEmpleado(empleadoC5)
    funeraria3.agregarEmpleado(empleadoC6)

    funeraria3.agregarEmpleado(empleadoF1)
    funeraria3.agregarEmpleado(empleadoF2)
    funeraria3.agregarEmpleado(empleadoF3)
    funeraria3.agregarEmpleado(empleadoF4)
    funeraria3.agregarEmpleado(empleadoF5)
    funeraria3.agregarEmpleado(empleadoF6)

    funeraria3.agregarEmpleado(empleadoP1)
    funeraria3.agregarEmpleado(empleadoP2)
    funeraria3.agregarEmpleado(empleadoP3)
    funeraria3.agregarEmpleado(empleadoP4)
    funeraria3.agregarEmpleado(empleadoP5)
    funeraria3.agregarEmpleado(empleadoP6)

    funeraria3.agregarEmpleado(empleadoO1)
    funeraria3.agregarEmpleado(empleadoO2)
    funeraria3.agregarEmpleado(empleadoO3)
    funeraria3.agregarEmpleado(empleadoO4)
    funeraria3.agregarEmpleado(empleadoO5)
    funeraria3.agregarEmpleado(empleadoO6)

    #Cuentas crematorio Funeraria 1
    cuentaF1Cr1= CuentaBancaria(103435, "Crematorio del Silencio",banco5, 2030)
    cuentaF1Cr2= CuentaBancaria(566506, "Ascenso y Tranquilidad",banco1, 20302)
    cuentaF1Cr3= CuentaBancaria(145044, "Brasa de Paz",banco2, 20302)
    cuentaF1Cr4= CuentaBancaria(120231, "Eterna Luz Crematorio",banco3, 20302)
    cuentaF1Cr5= CuentaBancaria(145066, "Crematorio del Renacer",banco4, 20302)
    cuentaF1Cr6= CuentaBancaria(156707, "Fuego y Serenidad",banco5, 20302)

    #Crematorio Funeraria 1
    crematorioF21 = Crematorio("Crematorio del Silencio", 100, cuentaF1Cr1, "oro", None, funeraria1)
    crematorioF22 = Crematorio("Ascenso y Tranquilidad", 78, cuentaF1Cr2, "oro", None, funeraria1)

    crematorioF23 = Crematorio("Brasa de Paz", 78, cuentaF1Cr3, "plata", None, funeraria1)
    crematorioF24 = Crematorio("Eterna Luz Crematorio", 78, cuentaF1Cr4, "plata", None, funeraria1)

    crematorioF25 = Crematorio("Crematorio del Renacer", 78, cuentaF1Cr5, "bronce", None, funeraria1)
    crematorioF26 = Crematorio("Fuego y Serenidad", 78, cuentaF1Cr6, "bronce", None, funeraria1)

    #Cuentas Cementerios Funeraria 1
    cuentaF1Ce1= CuentaBancaria(104525, "Jardín de la Eternidad",banco5, 2030)
    cuentaF1Ce2= CuentaBancaria(567576, "Colina de la Paz",banco1, 20302)
    cuentaF1Ce3= CuentaBancaria(145674, "Campos de tranquilidad",banco2, 20302)
    cuentaF1Ce4= CuentaBancaria(123424, "Valle del Silencio",banco3, 20302)
    cuentaF1Ce5= CuentaBancaria(175677, "Rincón del Descanso",banco4, 20302)
    cuentaF1Ce6= CuentaBancaria(175645, "Jardín de los Recuerdos",banco5, 20302)
    cuentaF1Ce7= CuentaBancaria(345345, "Eternidad Verde",banco1, 2030)
    cuentaF1Ce8= CuentaBancaria(567677, "Mirador de la Serenidad",banco2, 20302)
    cuentaF1Ce9= CuentaBancaria(132344, "Bosque de la Memoria",banco3, 20302)
    cuentaF1Ce10= CuentaBancaria(567567, "Cementerio del Refugi",banco4, 20302)
    cuentaF1Ce11= CuentaBancaria(678866, "Paz y Esperanza",banco5, 20302)
    cuentaF1Ce12= CuentaBancaria(123423, "Sendero de la Tranquilidad",banco1, 20302)
    
    #Cementerios Funeraria 1
    # Cementerios pertenecientes a F1 --> Funeraria 1 - cenizas
    cementerioF11Ce = Cementerio("Jardín de la Eternidad", 78, cuentaF1Ce1, "oro", None, "cenizas", funeraria1)
    cementerioF12Ce = Cementerio("Colina de la Paz", 85, cuentaF1Ce2, "oro", None, "cenizas", funeraria1)

    cementerioF13Ce = Cementerio("Campos de tranquilidad", 79, cuentaF1Ce3, "plata", None, "cenizas", funeraria1)
    cementerioF14Ce = Cementerio("Valle del Silencio", 78, cuentaF1Ce4, "plata", None, "cenizas", funeraria1)

    cementerioF15Ce = Cementerio("Rincón del Descanso", 50, cuentaF1Ce5, "bronce", None, "cenizas", funeraria1)
    cementerioF16Ce = Cementerio("Jardín de los Recuerdos", 78, cuentaF1Ce6, "bronce", None, "cenizas", funeraria1)

    # Cementerios pertenecientes a F1 --> Funeraria 1 - cuerpos
    cementerioF11Cu = Cementerio("Eternidad Verde", 78, cuentaF1Ce7, "oro", None, "cuerpos", funeraria1)
    cementerioF12Cu = Cementerio("Mirador de la Serenidad", 85, cuentaF1Ce8, "oro", None, "cuerpos", funeraria1)

    cementerioF13Cu = Cementerio("Bosque de la Memoria", 50, cuentaF1Ce9, "plata", None, "cuerpos", funeraria1)
    cementerioF14Cu = Cementerio("Cementerio del Refugi", 78, cuentaF1Ce10, "plata", None, "cuerpos", funeraria1)

    cementerioF15Cu = Cementerio("Paz y Esperanza", 78, cuentaF1Ce11, "bronce", None, "cuerpos", funeraria1)
    cementerioF16Cu = Cementerio("Sendero de la Tranquilidad", 78, cuentaF1Ce12, "bronce", None, "cuerpos", funeraria1)

    # Objetos Cementerio 1 Cenizas
    urnaF1C11 = Urna("Eterna Paz", cementerioF11Ce, 70, 1, "fija")
    urnaF1C12 = Urna("Memoria Serene", cementerioF11Ce, 80, 0, "ordinaria")
    urnaF1C13 = Urna("Descanso Sagrado", cementerioF11Ce, 60, 2, "ordinaria")
    urnaF1C14 = Urna("Luz Eterna", cementerioF11Ce, 60, 1, "fija")

    # Objetos Cementerio 2 Urna Cenizas
    urnaF1C21 = Urna("Tranquilidad Infinita", cementerioF12Ce, 70, 1, "fija")
    urnaF1C22 = Urna("Homenaje Perpetuo", cementerioF12Ce, 80, 0, "ordinaria")
    urnaF1C23 = Urna("Amanecer Sereno", cementerioF12Ce, 70, 2, "ordinaria")
    urnaF1C24 = Urna("Refugio del Alma", cementerioF12Ce, 60, 1, "fija")

    # Objetos Cementerio 3 Urna Cenizas
    urnaF1C31 = Urna("Oasis de Recuerdo", cementerioF13Ce, 70, 1, "fija")
    urnaF1C32 = Urna("Sombra Amada", cementerioF13Ce, 80, 0, "ordinaria")
    urnaF1C33 = Urna("Caja de la Verdad", cementerioF13Ce, 50, 2, "ordinaria")
    urnaF1C34 = Urna("Urna Democracia", cementerioF13Ce, 60, 1, "fija")

    # Objetos Cementerio 4 Urna Cenizas
    urnaF1C41 = Urna("Voz del Pueblo", cementerioF14Ce, 70, 1, "fija")
    urnaF1C42 = Urna("Cámara Decisiones", cementerioF14Ce, 80, 0, "ordinaria")
    urnaF1C43 = Urna("Bóveda Opiniones", cementerioF14Ce, 70, 0, "ordinaria")
    urnaF1C44 = Urna("Recinto Electoral", cementerioF14Ce, 60, 1, "fija")

    # Objetos Cementerio 5 Urna Cenizas
    urnaF1C51 = Urna("Contenedor Voluntades", cementerioF15Ce, 70, 1, "fija")
    urnaF1C52 = Urna("Caja de Equidad", cementerioF15Ce, 80, 0, "ordinaria")
    urnaF1C53 = Urna("Justicia", cementerioF15Ce, 70, 0, "ordinaria")
    urnaF1C54 = Urna("Escudo Electoral", cementerioF15Ce, 60, 1, "fija")

    # Objetos Cementerio 6 Urna Cenizas
    urnaF1C61 = Urna("Cápsula de Sueños", cementerioF16Ce, 70, 1, "fija")
    urnaF1C62 = Urna("Templo Belleza", cementerioF16Ce, 80, 0, "ordinaria")
    urnaF1C63 = Urna("Misterio Dorado", cementerioF16Ce, 60, 0, "ordinaria")
    urnaF1C64 = Urna("Joyero Recuerdos", cementerioF16Ce, 60, 1, "fija")

    #CuentasBancarias empleados sepulteros funeraria 1
    cuentaF1ESe1= CuentaBancaria(562344, "Adrián Vargas",banco1, 20302)
    cuentaF1ESe2= CuentaBancaria(145444, "Benjamín Díaz",banco2, 20302)
    cuentaF1ESe3= CuentaBancaria(567775, "Cristian Herrera",banco3, 20302)
    cuentaF1ESe4= CuentaBancaria(134534, "Diana Moreno",banco4, 20302)
    cuentaF1ESe5= CuentaBancaria(789899, "Gabriela Arias",banco5, 20302)

    #Empleados sepulturero
    
    empleadoF11S = Empleado("Adrián Vargas", cuentaF1ESe1, "mañana", "sepulturero", 1000000, funeraria1)
    empleadoF12S = Empleado("Benjamín Díaz", cuentaF1ESe2, "mañana", "sepulturero", 1000000, funeraria1)
    empleadoF13S = Empleado("Cristian Herrera", cuentaF1ESe3, "tarde", "sepulturero", 1000000, funeraria1)
    empleadoF14S = Empleado("Diana Moreno", cuentaF1ESe4, "tarde", "sepulturero", 1000000, funeraria1)
    empleadoF15S = Empleado("Gabriela Arias", cuentaF1ESe5, "noche", "sepulturero", 1000000, funeraria1)
    
    #CuentasBancarias empleados cremadores funeraria 1
    cuentaF1ECr1= CuentaBancaria(523424, "David Soto",banco1, 20302)
    cuentaF1ECr2= CuentaBancaria(167868, "Esteban Cordero",banco2, 20302)
    cuentaF1ECr3= CuentaBancaria(523424, "Federico Gil",banco3, 20302)
    cuentaF1ECr4= CuentaBancaria(112313, "Elena Vázquez",banco4, 20302)
    cuentaF1ECr5= CuentaBancaria(767888, "Isabela López",banco5, 20302)

    # Empleados cremador

    empleadoF11C = Empleado("David Soto", cuentaF1ECr1, "mañana", "cremador", 1000000, funeraria1)
    empleadoF12C = Empleado("Esteban Cordero", cuentaF1ECr2, "mañana", "cremador", 1000000, funeraria1)
    empleadoF13C = Empleado("Federico Gil", cuentaF1ECr3, "tarde", "cremador", 1000000, funeraria1)
    empleadoF14C = Empleado("Elena Vázquez", cuentaF1ECr4, "noche", "cremador", 1000000, funeraria1)
    empleadoF15C = Empleado("Isabela López", cuentaF1ECr5, "noche", "cremador", 1000000, funeraria1)
   
    #Cuentas familiares 
    cuentaFa1= CuentaBancaria(534555, "Mario",banco1, 2030)
    cuentaFa2= CuentaBancaria(167886, "Alberto",banco2, 2030212)
    cuentaFa3= CuentaBancaria(580809, "Carlos",banco3, 20302)
    cuentaFa4= CuentaBancaria(118099, "Samantha",banco4, 203021)

    #Familiares
    F11 = Familiar("Mario", 711, 50, cuentaFa1, "padre", 17)
    F12 = Familiar("Alberto", 712, 32, cuentaFa2, "conyuge", 13)
    F13 = Familiar("Carlos", 713, 37, cuentaFa3, "hermano", 17)
    F14 = Familiar("Samantha", 714, 50, cuentaFa4, "padre", 17)
    
    FamiliarF11=[F11,F12,F13,F14]
    
    #cuentas clientes funeraria 1
    cuentaF1Cl1= CuentaBancaria(512313, "Alejandro Rodríguez",banco1, 203032)
    cuentaF1Cl2= CuentaBancaria(112222, "Diego Martínez", banco2, 2030)
    cuentaF1Cl3= CuentaBancaria(124444, "Carlos Fernández",banco3, 20304)
    cuentaF1Cl4= CuentaBancaria(176666, "María González",banco4, 203024)
    cuentaF1Cl5= CuentaBancaria(179999, "Laura Fernández",banco5, 2030232)
    cuentaF1Cl6= CuentaBancaria(348888, "Isabel Rodríguez",banco1, 203022)
    
    #Clientes de la funeraria 1 mayores de edad
    clienteF11 = Cliente("Alejandro Rodríguez",123,30,cuentaF1Cl1,"oro",FamiliarF11)
    clienteF12 = Cliente("Diego Martínez",1234,25,cuentaF1Cl2,"oro",FamiliarF11)	
    clienteF13 = Cliente("Carlos Fernández",1235,90,cuentaF1Cl3,"plata",FamiliarF11)
    clienteF14 = Cliente("María González",1236,57,cuentaF1Cl4, "plata",FamiliarF11)
    clienteF15 = Cliente("Laura Fernández",1237,21, cuentaF1Cl5,"bronce",FamiliarF11)
    clienteF16 = Cliente("Isabel Rodríguez",1238,50,cuentaF1Cl6,"bronce",FamiliarF11)
	
		
	#Clientes F1 - Menores de edad
    clienteF17 = Cliente("Javier Gómez",0,5,None,"oro",FamiliarF11)
    clienteF18 = Cliente("Sofía Martínez",0,17,None,"oro",FamiliarF11)
    clienteF19 = Cliente("Carolina López",0,15,None,"plata",FamiliarF11)
    clienteF110= Cliente("Manuel López",0,13,None,"plata",FamiliarF11)
		
	
	#AgregarClientes
    funeraria1.agregarCliente(clienteF11)
    funeraria1.agregarCliente(clienteF12)
    funeraria1.agregarCliente(clienteF13)
    funeraria1.agregarCliente(clienteF14)
    funeraria1.agregarCliente(clienteF15)
    funeraria1.agregarCliente(clienteF16)
    funeraria1.agregarCliente(clienteF17)
    funeraria1.agregarCliente(clienteF18)
    funeraria1.agregarCliente(clienteF19)
    funeraria1.agregarCliente(clienteF110)



    #Funcionalidad exhumacion

    #Familiares

    #Cuentas familiares mujeres
    cuentaFAM1 = CuentaBancaria(274784,"Mario",banco1,123543)
    cuentaFAM2 = CuentaBancaria(273454,"Alberto",banco2,12354)
    cuentaFAM3 = CuentaBancaria(234556,"Carlos",banco3,1235)
    cuentaFAM4 = CuentaBancaria(273456,"Samantha",banco4,123543)

    # Familiares Mujeres
    F11 = Familiar("Mario", 711, 50, cuentaFAM1, "padre", 17)
    F12 = Familiar("Alberto", 712, 32, cuentaFAM2, "conyuge", 13)
    F13 = Familiar("Carlos", 713, 37, cuentaFAM3, "hermano", 17)
    F14 = Familiar("Samantha", 714, 50, cuentaFAM4, "padre", 17)

    #Cuentas familiares para todos
    cuentaFAM1 = CuentaBancaria(274566,"Samuel",banco1,12354)
    cuentaFAM2 = CuentaBancaria(345500,"Alma",banco2,123543)
    cuentaFAM3 = CuentaBancaria(325605,"Eduardo",banco3,1235333)
    cuentaFAM4 = CuentaBancaria(223805,"Maria",banco4,123543)

    # Familiares para todos
    F15 = Familiar("Samuel", 715, 60, cuentaFAM1, "padre", 17)
    F16 = Familiar("Alma", 716, 60, cuentaFAM2, "padre", 13)
    F17 = Familiar("Eduardo", 717, 37, cuentaFAM3, "hermano", 17)
    F18 = Familiar("Maria", 0,5,cuentaFAM4, "hermano", F17)
 
    #Cuentas familiares hombre
    cuentaFAH1 = CuentaBancaria(274567,"Armando",banco1,123544)
    cuentaFAH2 = CuentaBancaria(345345,"Catalina",banco2,12355)
    cuentaFAH3 = CuentaBancaria(324567,"Sebastian",banco3,12353)
    cuentaFAH4 = CuentaBancaria(212333,"Alba",banco4,123543)
    
    # Familiares Hombres
    F19 = Familiar("Armando", 718, 50, cuentaFAH1, "padre", 17)
    F110 = Familiar("Catalina", 719, 32, cuentaFAH2, "conyuge", 13)
    F111 = Familiar("Sebastian", 7110, 37, cuentaFAH3, "hermano", 17)
    F112 = Familiar("Alba", 7111, 25, cuentaFAH4, "hijo", 17)
    
    #Listas de familiares A
    familiarA=[]
    familiarA.append(F11)
    familiarA.append(F12)
    familiarA.append(F13)
    familiarA.append(F14)
		
    #Listas de familiares B
    familiarB=[]
    familiarB.append(F15)
    familiarB.append(F16)
    familiarB.append(F17)
    familiarB.append(F18)

    #Listas de familiares C
    familiarC=[]
    familiarC.append(F19)
    familiarC.append(F110)
    familiarC.append(F111)
    familiarC.append(F112)
	
    #Cuenta clientes urnas
    cuentaCU1 = CuentaBancaria(223455, "Juan Pérez", banco1, 2252545)
    cuentaCU2 = CuentaBancaria(233211, "Carlos Fernández", banco2, 225245)
    cuentaCU3 = CuentaBancaria(123462, "Miguel Rodríguez", banco3, 22525)
    cuentaCU4 = CuentaBancaria(256788, "Dani Morales", banco4, 22525)
    cuentaCU5 = CuentaBancaria(238558, "Pedro González", banco5, 225254)
    cuentaCU6 = CuentaBancaria(678086, "José Martínez", banco1, 225254)
    cuentaCU11 = CuentaBancaria(223456, "Laura Morales", banco1, 22525)
    cuentaCU12 = CuentaBancaria(245678, "Robert Jones", banco2, 225254)
    cuentaCU13 = CuentaBancaria(267899, "Olivia Miller", banco3, 2252545)
    cuentaCU14 = CuentaBancaria(223677, "Sophia Moore", banco4, 225254)

    clienteF11E = Cliente("Juan Pérez", 511, 30, cuentaCU1, "oro", FamiliarF11)
    clienteF12E = Cliente("Carlos Fernández", 512, 25, cuentaCU2, "oro", FamiliarF11)

    clienteF13E = Cliente("Miguel Rodríguez", 513, 90, cuentaCU3, "plata", FamiliarF11)
    clienteF14E = Cliente("Dani Morales", 514, 57, cuentaCU4, "plata", FamiliarF11)

    clienteF15E = Cliente("Pedro González", 515, 50, cuentaCU5, "bronce", FamiliarF11)
    clienteF16E = Cliente("José Martínez", 516, 30, cuentaCU6, "bronce", FamiliarF11)

    clienteF17E = Cliente("María López",0,5,None,"oro",familiarB)
    clienteF18E = Cliente("Carmen García",0,17,None,"oro",familiarB)
										
    clienteF19E = Cliente("Ana Torres",0,15,None,"bronce",familiarB)
    clienteF110E = Cliente("Isabel Ramírez",0,13,None,"bronce",familiarB)
		
    clienteF111E = Cliente("Laura Morales",5111,90,cuentaCU11,"plata",familiarA)
    clienteF112E = Cliente("Robert Jones",5112,57,cuentaCU12,"plata",familiarC)
								
    clienteF113E = Cliente("Olivia Miller",5113,35,cuentaCU13, "bronce",familiarC)
    clienteF114E = Cliente("Sophia Moore",5114,50,cuentaCU14, "bronce",familiarC)
		
    clienteF115E = Cliente("James Smith",0,5,None,"oro",familiarB)
    clienteF116E = Cliente("David Brown",0,17,None,"oro",familiarB)
										
    clienteF117E = Cliente("John Williams",0,15,None,"bronce",familiarB)
    clienteF118E = Cliente("Michael Johnson",0,13,None,"bronce",familiarB)
		

		
	#Cementerio 1 Cenizas
    urnaF1C11E=Urna("Esperanza",cementerioF11Ce,70,1,"fija")
    urnaF1C12E=Urna("Futuro",cementerioF11Ce,80,0,"fija")
    urnaF1C13E=Urna("default",cementerioF11Ce,50,0,"fija")
		
    urnaF1C14E=Urna("Esperanza",cementerioF11Ce,70,1,"fija")
    urnaF1C15E=Urna("Futuro",cementerioF11Ce,80,0,"fija")
		
	#Cementerio 2 Cenizas
    urnaF1C21E=Urna("Sabiduría",cementerioF12Ce,70,1,"fija")
    urnaF1C22E=Urna("Justicia",cementerioF12Ce,80,0,"fija")
    urnaF1C23E=Urna("default",cementerioF12Ce,90,0,"fija")
		
    urnaF1C24E=Urna("Sabiduría",cementerioF12Ce,70,1,"fija")
    urnaF1C25E=Urna("Justicia",cementerioF12Ce,80,0,"fija")
		
	#Cementerio 3 Cenizas
    urnaF1C31E=Urna("Confianza",cementerioF13Ce,70,1,"fija")
    urnaF1C32E=Urna("Progreso",cementerioF13Ce,80,0,"fija")
    urnaF1C33E=Urna("default",cementerioF13Ce,90,0,"fija")
		
    urnaF1C34E=Urna("Confianza",cementerioF13Ce,70,1,"fija")
    urnaF1C35E=Urna("Progreso",cementerioF13Ce,80,0,"fija")
	
		
	#Cementerio 4 Cenizas
    urnaF1C41E=Urna("Verdadera Voz",cementerioF14Ce,70,1,"fija")
    urnaF1C42E=Urna("Decisión",cementerioF14Ce,80,0,"fija")
    urnaF1C43E=Urna("default",cementerioF14Ce,60,0,"fija")
		
    urnaF1C44E=Urna("Verdadera Voz",cementerioF14Ce,70,1,"fija")
    urnaF1C45E=Urna("Decisión",cementerioF14Ce,80,0,"fija")
		
	#Cementerio 5 Cenizas
    urnaF1C51E=Urna("Cambio",cementerioF15Ce,70,1,"fija")
    urnaF1C52E=Urna("Pueblo",cementerioF15Ce,80,0,"fija")
    urnaF1C53E=Urna("default",cementerioF15Ce,60,0,"ordinaria")
		
    urnaF1C54E=Urna("Cambio",cementerioF15Ce,70,1,"fija")
    urnaF1C55E=Urna("Pueblo",cementerioF15Ce,80,0,"fija")
	
		
	#Cementerio 6 Cenizas
    urnaF1C61E=Urna("Transparencia",cementerioF16Ce,70,1,"fija")
    urnaF1C62E=Urna("Compromiso",cementerioF16Ce,80,0,"fija")
    urnaF1C63E=Urna("default",cementerioF16Ce,60,0,"ordinaria")
		
    urnaF1C64E=Urna("Transparencia",cementerioF16Ce,70,1,"fija")
    urnaF1C65E=Urna("Compromiso",cementerioF16Ce,80,0,"fija")
	
    #Agregar clientes
		
    urnaF1C11E.agregarCliente(clienteF11E)
    urnaF1C12E.agregarCliente(clienteF12E)
    urnaF1C13E.agregarCliente(clienteF13E)
		
    urnaF1C21E.agregarCliente(clienteF14E)
    urnaF1C22E.agregarCliente(clienteF15E)
    urnaF1C23E.agregarCliente(clienteF16E)
		
    urnaF1C31E.agregarCliente(clienteF17E)
    urnaF1C32E.agregarCliente(clienteF18E)
    urnaF1C33E.agregarCliente(clienteF19E)
		
    urnaF1C41E.agregarCliente(clienteF110E)
    urnaF1C42E.agregarCliente(clienteF111E)
    urnaF1C43E.agregarCliente(clienteF112E)
		
    urnaF1C51E.agregarCliente(clienteF113E)
    urnaF1C52E.agregarCliente(clienteF114E)
    urnaF1C53E.agregarCliente(clienteF115E)
		
    urnaF1C61E.agregarCliente(clienteF116E)
    urnaF1C62E.agregarCliente(clienteF117E)
    urnaF1C63E.agregarCliente(clienteF118E)

    #Cuentas clientes tumbas 
    cuentaCT1 = CuentaBancaria(174647,"Ezequiel Andrade", banco1, 463483)
    cuentaCT2 = CuentaBancaria(172356,"Damián Vargas", banco1, 46348)
    cuentaCT3 = CuentaBancaria(134667,"Octavio Salazar", banco1, 463483)
    cuentaCT4 = CuentaBancaria(578678,"Leonardo Paredes", banco1, 46348)
    cuentaCT5 = CuentaBancaria(134506,"Ulises Ortega", banco1, 46383)
    cuentaCT6 = CuentaBancaria(139600,"Valeria Castro", banco1, 46383)
    cuentaCT7 = CuentaBancaria(172567,"Leo Cruz", banco1, 463483)
    cuentaCT8 = CuentaBancaria(112444,"Luna Martínez", banco1, 4634354)
    cuentaCT9 = CuentaBancaria(134585,"Lucas Moreno", banco1, 46383)
    cuentaCT10 = CuentaBancaria(384848,"Sofía Rodríguez", banco1, 63483)
    # Clientes para tumbas

    clienteF11ET = Cliente("Ezequiel Andrade", 611, 30, cuentaCT1, "oro", familiarC)
    clienteF12ET = Cliente("Damián Vargas", 612, 25, cuentaCT2, "oro", familiarC)

    clienteF13ET = Cliente("Octavio Salazar", 613, 90, cuentaCT3, "plata", familiarB)
    clienteF14ET = Cliente("Leonardo Paredes", 614, 57, cuentaCT4, "plata", familiarB)

    clienteF15ET = Cliente("Ulises Ortega", 615, 21, cuentaCT5, "bronce", familiarC)
    clienteF16ET = Cliente("Valeria Castro", 616, 50, cuentaCT6, "bronce", familiarC)

    clienteF17ET = Cliente("Delfina Méndez", 0,5, None,"oro", familiarB)
    clienteF18ET = Cliente("Mireya Delgado", 0,17,None, "oro", familiarB)

    clienteF19ET = Cliente("Renata Aguirre",0, None,15, "plata", familiarB)
    clienteF110ET = Cliente("Alma Guzmán", 0, None,13, "plata", familiarB)

    clienteF111ET = Cliente("Leo Cruz", 6111, 90, cuentaCT7, "plata", familiarB)
    clienteF112ET = Cliente("Luna Martínez", 6112, 57, cuentaCT8, "plata", familiarB)

    clienteF113ET = Cliente("Lucas Moreno", 6113, 21, cuentaCT9, "bronce", familiarC)
    clienteF114ET = Cliente("Sofía Rodríguez", 1238, 50, cuentaCT10, "bronce", familiarC)

    # Clientes F1 - Menores de edad
    clienteF115ET = Cliente("Aitana Gómez", 0,5,None, "oro", familiarB)
    clienteF116ET = Cliente("Zoe García", 0,17, None,"oro", familiarB)

    clienteF117ET = Cliente("Ethan Ortega", 0,15,None, "plata", familiarB)
    clienteF118ET = Cliente("Dylan Mendoza", 0,13,None, "plata", familiarB)

    # Cementerio 1
    tumbaF1C11E = Tumba("Tumbita Lugar de Paz", cementerioF11Cu, 1.70, 1)
    tumbaF1C12E = Tumba("Tumbita Descanso Eterno", cementerioF11Cu, 1.50, 0)
    tumbaF1C13E = Tumba("default", cementerioF11Cu, 1.70, 0)

    tumbaF1C15E = Tumba("Tumbita Lugar de Paz", cementerioF11Cu, 1.70, 1)
    tumbaF1C16E = Tumba("Tumbita Descanso Eterno", cementerioF11Cu, 1.50, 0)

    # Cementerio 2
    tumbaF1C21E = Tumba("Tumbita Siempre Recordado", cementerioF12Cu, 1.70, 1)
    tumbaF1C22E = Tumba("Tumbita En Honor a un Ser Querido", cementerioF12Cu, 1.60, 0)
    tumbaF1C23E = Tumba("default", cementerioF12Cu, 1.60, 0)

    tumbaF1C25E = Tumba("Tumbita Siempre Recordado", cementerioF12Cu, 1.70, 1)
    tumbaF1C26E = Tumba("Tumbita En Honor a un Ser Querido", cementerioF12Cu, 1.60, 0)

    # Cementerio 3
    tumbaF1C31E = Tumba("Tumbita Lugar de Serenidad", cementerioF13Cu, 1.70, 1)
    tumbaF1C32E = Tumba("Tumbita Eterna Paz", cementerioF13Cu, 1.65, 0)
    tumbaF1C33E = Tumba("default", cementerioF13Cu, 1.75, 0)

    tumbaF1C34E = Tumba("Tumbita Lugar de Serenidad", cementerioF13Cu, 1.70, 1)
    tumbaF1C35E = Tumba("Tumbita Eterna Paz", cementerioF13Cu, 1.65, 0)

    # Cementerio 4
    tumbaF1C41E = Tumba("Tumbita Un Alma Bella", cementerioF14Cu, 1.70, 1)
    tumbaF1C42E = Tumba("Tumbita En Paz y Serenidad", cementerioF14Cu, 1.70, 0)
    tumbaF1C43E = Tumba("default", cementerioF14Cu, 1.55, 0)

    tumbaF1C44E = Tumba("Tumbita Un Alma Bella", cementerioF14Cu, 1.70, 1)
    tumbaF1C45E = Tumba("Tumbita En Paz y Serenidad", cementerioF14Cu, 1.70, 0)

    # Cementerio 5
    tumbaF1C51E = Tumba("Tumbita Siempre en Nuestros Corazones", cementerioF15Cu, 1.70, 1)
    tumbaF1C52E = Tumba("Tumbita Aquí Descansa en Paz", cementerioF15Cu, 1.50, 0)
    tumbaF1C53E = Tumba("default", cementerioF15Cu, 1.55, 0)

    tumbaF1C54E = Tumba("Tumbita Siempre en Nuestros Corazones", cementerioF15Cu, 1.70, 1)
    tumbaF1C55E = Tumba("Tumbita Aquí Descansa en Paz", cementerioF15Cu, 1.50, 0)

    # Cementerio 6
    tumbaF1C61E = Tumba("Tumbita La Luz de Nuestra Vida", cementerioF16Cu, 1.70, 1)
    tumbaF1C62E = Tumba("Tumbita Aquí La Memoria Vive", cementerioF16Cu, 1.60, 0)
    tumbaF1C63E = Tumba("default", cementerioF16Cu, 1.60, 0)

    tumbaF1C64E = Tumba("Tumbita La Luz de Nuestra Vida", cementerioF16Cu, 1.70, 1)
    tumbaF1C65E = Tumba("Tumbita Aquí La Memoria Vive", cementerioF16Cu, 1.60, 0)

    # Agregar clientes a tumbas
    tumbaF1C11E.agregarCliente(clienteF11ET)
    tumbaF1C12E.agregarCliente(clienteF12ET)
    tumbaF1C13E.agregarCliente(clienteF13ET)

    tumbaF1C21E.agregarCliente(clienteF14ET)
    tumbaF1C22E.agregarCliente(clienteF15ET)
    tumbaF1C23E.agregarCliente(clienteF16ET)

    tumbaF1C31E.agregarCliente(clienteF17ET)
    tumbaF1C32E.agregarCliente(clienteF18ET)
    tumbaF1C33E.agregarCliente(clienteF19ET)

    tumbaF1C41E.agregarCliente(clienteF110ET)
    tumbaF1C42E.agregarCliente(clienteF111ET)
    tumbaF1C43E.agregarCliente(clienteF112ET)

    tumbaF1C51E.agregarCliente(clienteF113ET)
    tumbaF1C52E.agregarCliente(clienteF114ET)
    tumbaF1C53E.agregarCliente(clienteF115ET)

    tumbaF1C61E.agregarCliente(clienteF116ET)
    tumbaF1C62E.agregarCliente(clienteF117ET)
    tumbaF1C63E.agregarCliente(clienteF118ET)


    #Funeraria 2
    # Empleados sepultureros
    empleadoF21S = Empleado("Guillermo Romero", None, "mañana", "sepulturero", 1000000, funeraria2)
    empleadoF22S = Empleado("Jorge Álvarez", None, "tarde", "sepulturero", 1000000, funeraria2)
    empleadoF23S = Empleado("Florencia Pérez", None, "tarde", "sepulturero", 1000000, funeraria2)
    empleadoF24S = Empleado("Jazmín Navarro", None, "tarde", "sepulturero", 1000000, funeraria2)
    empleadoF25S = Empleado("Alicia Moreno", None, "noche", "sepulturero", 1000000, funeraria2)

    # Empleados cremador
    empleadoF21C = Empleado("Marco Ruiz", None, "noche", "cremador", 1000000, funeraria2)
    empleadoF22C = Empleado("Natalia Ortega", None, "mañana", "cremador", 1000000, funeraria2)
    empleadoF23C = Empleado("Casey Morales", None, "tarde", "cremador", 1000000, funeraria2)
    empleadoF24C = Empleado("Karla Soto", None, "noche", "cremador", 1000000, funeraria2)
    empleadoF25C = Empleado("Dakota Torres", None, "noche", "cremador", 1000000, funeraria2)
	
    
    #Familiares
    # Creación de instancias de Familiar

    F21 = Familiar("Ophelia", 12345, 18, None, "conyugue", 17)
    F22 = Familiar("Atticus", 12375, 70, None, "padre", 17)
    F23 = Familiar("Lyriel", 0,12, None,"hijo",0,F21)
    F24 = Familiar("Andres", 0,5, None,"hermano",0,F21)

    F25 = Familiar("Libia", 12345, 18, None, "conyugue", 17)
    F26 = Familiar("Armando", 12375, 70, None, "padre", 17)
    F27 = Familiar("Lyriel", 0,12, None,"hijo",0,F26)
    F28 = Familiar("Andres", 0,5, None,"hermano",0,F25)

    F29 = Familiar("Andres", 12345, 18, None, "conyugue", 17)
    F210 = Familiar("Catalina", 12375, 70, None, "padre", 17)
    F211 = Familiar("Lyriel", 0,12, None,"hijo",0,F29)
    F212 = Familiar("Andres", 0,5, None,"hermano",0,F29)

    F213 = Familiar("Alma", 715, 60, None, "padre", 17)
    F214 = Familiar("Mar", 716, 60, None, "padre", 13)
    F215 = Familiar("Eduardo", 717, 37, None, "hermano", 17)
    F216 = Familiar("Andres", 0,5, None,"hermano",0,F214)

    F217 = Familiar("Carmen", 715, 60, None, "padre", 17)
    F218 = Familiar("Catalina", 716, 60, None, "padre", 13)
    F219 = Familiar("Carlos", 717, 37, None, "hermano", 17)
    F220 = Familiar("Andres", 0,5, None,"hermano",0,F217)

    F221 = Familiar("Pablo", 715, 60, None, "padre", 17)
    F222 = Familiar("Sol", 716, 60, None, "padre", 13)
    F223 = Familiar("Andres", 717, 37, None, "hermano", 17)
    F224 = Familiar("Andres", 0,5, None,"hermano",0,F221)

    
    # Lista de familiares G
    familiarG = [F21, F22, F23, F24]

    # Lista de familiares H
    familiarH = [F25, F26, F27, F28]

    # Lista de familiares I
    familiarI = [F29, F210, F211, F212]

    # Lista de familiares J
    familiarJ = [F213, F214, F215, F216]

    # Lista de familiares K
    familiarK = [F217, F218, F219, F220]

    # Lista de familiares L
    familiarL = [F221, F222, F223, F224]
    
    # Creación de instancias de Familiar
    F21M = Familiar("Camila", 715, 60, None, "padre", 17)
    F22M = Familiar("Luis", 716, 60, None, "padre", 13)
    F23M = Familiar("Tomas", 717, 37, None, "hermano", 17)
    F24M = Familiar("Andres", 717, 37, None, "hermano", 17)

    F25M = Familiar("Vanesa", 715, 60, None, "padre", 17)
    F26M = Familiar("Carlos", 716, 60, None, "padre", 13)
    F27M = Familiar("Juan Jose", 717, 37, None, "hermano", 17)
    F28M = Familiar("Nicolas", 717, 37, None, "hermano", 17)

    F29M = Familiar("Mateo", 715, 60, None, "padre", 17)
    F210M = Familiar("Mariana", 716, 60, None, "padre", 13)
    F211M = Familiar("Esteban", 717, 37, None, "hermano", 17)
    F212M = Familiar("David", 717, 37, None, "hermano", 17)

    F213M = Familiar("Jireh", 715, 60, None, "padre", 17)
    F214M = Familiar("Carlos", 716, 60, None, "padre", 13)
    F215M = Familiar("Carla", 717, 37, None, "hermano", 17)
    F216M = Familiar("Carolina", 717, 37, None, "hermano", 17)

    # Lista de familiares EM
    familiarEM = [F21M, F22M, F23M, F24M]

    # Lista de familiares FM
    familiarFM = [F25M, F26M, F27M, F28M]

    # Lista de familiares GM
    familiarGM = [F29M, F210M, F211M, F212M]

    # Lista de familiares HM
    familiarHM = [F213M, F214M, F215M, F216M]

    # Supongamos que cuenta13CE, cuenta14CE, ..., cuenta24CE ya están definidos
    cuenta13CE = "cuenta13CE"
    cuenta14CE = "cuenta14CE"
    cuenta15CE = "cuenta15CE"
    cuenta16CE = "cuenta16CE"   
    cuenta17CE = "cuenta17CE"
    cuenta18CE = "cuenta18CE"
    cuenta19CE = "cuenta19CE"
    cuenta20CE = "cuenta20CE"
    cuenta21CE = "cuenta21CE"
    cuenta22CE = "cuenta22CE"
    cuenta23CE = "cuenta23CE"
    cuenta24CE = "cuenta24CE"


    # Cementerios pertenecientes a F2 --> Funeraria 2 - cenizas
    cementerioF21Ce = Cementerio("Cementerio del Silencio", 78, cuenta13CE, "oro", None, "cenizas", funeraria2)
    cementerioF22Ce = Cementerio("Campo de la Eternidad", 85, cuenta14CE, "oro", None, "cenizas", funeraria2)
    cementerioF23Ce = Cementerio("Bosque de la Serenidad", 79, cuenta15CE, "plata", None, "cenizas", funeraria2)
    cementerioF24Ce = Cementerio("Jardines del Descanso", 78, cuenta16CE, "plata", None, "cenizas", funeraria2)
    cementerioF25Ce = Cementerio("Valle de la Paz Interior", 50, cuenta17CE, "bronce", None, "cenizas", funeraria2)
    cementerioF26Ce = Cementerio("Luz del Recuerdo", 78, cuenta18CE, "bronce", None, "cenizas", funeraria2)

    # Cementerios pertenecientes a F2 --> Funeraria 2 - cuerpos
    cementerioF21Cu = Cementerio("Colinas del Reposo", 78, cuenta19CE, "oro", None, "cuerpos", funeraria2)
    cementerioF22Cu = Cementerio("Jardín de la Eternidad", 85, cuenta20CE, "oro", None, "cuerpos", funeraria2)
    cementerioF23Cu = Cementerio("Refugio de la Memoria", 50, cuenta21CE, "plata", None, "cuerpos", funeraria2)
    cementerioF24Cu = Cementerio("Cementerio del Alba", 78, cuenta22CE, "plata", None, "cuerpos", funeraria2)
    cementerioF25Cu = Cementerio("Alameda de la Paz", 78, cuenta23CE, "bronce", None, "cuerpos", funeraria2)
    cementerioF26Cu = Cementerio("Jardín del Silencio Eterno", 78, cuenta24CE, "bronce", None, "cuerpos", funeraria2)

    # Cementerio 1 Cenizas
    urnaF2C11 = Urna("Urnita Eterna Paz", cementerioF21Ce, 70, 1, "fija")
    urnaF2C12 = Urna("Urnita Memoria Serene", cementerioF21Ce, 80, 0, "fija")
    urnaF2C13 = Urna("Urnita Descanso Sagrado", cementerioF21Ce, 50, 0, "ordinaria")
    urnaF2C14 = Urna("Urnita Luz Eterna", cementerioF21Ce, 60, 1, "fija")

    # Cementerio 2 Urna Cenizas
    urnaF2C21 = Urna("Urnita Tranquilidad Infinita", cementerioF22Ce, 50, 1, "fija")
    urnaF2C22 = Urna("Urnita Homenaje Perpetuo", cementerioF22Ce, 80, 0, "ordinaria")
    urnaF2C23 = Urna("Urnita Amanecer Sereno", cementerioF22Ce, 70, 0, "ordinaria")
    urnaF2C24 = Urna("Urnita Refugio del Alma", cementerioF22Ce, 60, 1, "ordinaria")

    # Cementerio 3 Urna Cenizas
    urnaF2C31 = Urna("Urnita Oasis de Recuerdo", cementerioF23Ce, 60, 1, "fija")
    urnaF2C32 = Urna("Urnita Sombra Amada", cementerioF23Ce, 50, 0, "ordinaria")
    urnaF2C33 = Urna("Urnita Caja de la Verdad", cementerioF23Ce, 60, 2, "ordinaria")
    urnaF2C34 = Urna("Urnita Urna de la Democracia", cementerioF23Ce, 60, 1, "fija")

    # Cementerio 4 Urna Cenizas
    urnaF2C41 = Urna("Urnita Voz del Pueblo", cementerioF24Ce, 70, 1, "fija")
    urnaF2C42 = Urna("Urnita Cámara de Decisiones", cementerioF24Ce, 80, 0, "ordinaria")
    urnaF2C43 = Urna("Urnita Bóveda de Opiniones", cementerioF24Ce, 70, 0, "ordinaria")
    urnaF2C44 = Urna("Urnita Recinto Electoral", cementerioF24Ce, 60, 1, "fija")

    # Cementerio 5 Urna Cenizas
    urnaF2C51 = Urna("Urnita Contenedor de Voluntades", cementerioF25Ce, 70, 1, "fija")
    urnaF2C52 = Urna("Urnita Caja de Equidad", cementerioF25Ce, 80, 1, "ordinaria")
    urnaF2C53 = Urna("Urnita de la Justicia", cementerioF25Ce, 50, 2, "ordinaria")
    urnaF2C54 = Urna("Urnita Escudo Electoral", cementerioF25Ce, 60, 1, "fija")

    # Cementerio 6 Urna Cenizas
    urnaF2C61 = Urna("Urnita Cápsula de Sueños", cementerioF26Ce, 70, 1, "fija")
    urnaF2C62 = Urna("Urnita Templo de Belleza", cementerioF26Ce, 80, 0, "ordinaria")
    urnaF2C63 = Urna("Urnita Misterio Dorado", cementerioF26Ce, 40, 0, "ordinaria")
    urnaF2C64 = Urna("Urnita Joyero de Recuerdos", cementerioF26Ce, 60, 1, "fija")

    # Cementerio 1 Tumbas Cuerpos
    tumbaF2C11 = Tumba("Tumbita Aquí Reposa un Corazón Noble", cementerioF21Cu, 1.70, 1)
    tumbaF2C12 = Tumba("Tumbita Amado por Siempre", cementerioF21Cu, 1.60, 0)
    tumbaF2C13 = Tumba("Tumbita Siempre en Nuestros Corazones", cementerioF21Cu, 1.60, 1)
    tumbaF2C14 = Tumba("Tumbita Un Alma Inmortal", cementerioF21Cu, 1.20, 1)
    tumbaF2C15 = Tumba("Tumbita Tu Luz Nos Guía", cementerioF21Cu, 1.55, 2)
    tumbaF2C16 = Tumba("Tumbita Querido y Recordado", cementerioF21Cu, 1.50, 2)

    # Cementerio 2 Tumbas Cuerpos
    tumbaF2C21 = Tumba("Tumbita Descansa en Paz, Amado", cementerioF22Cu, 1.70, 0)
    tumbaF2C22 = Tumba("Tumbita Tu Memoria Vive en Nosotros", cementerioF22Cu, 1.60, 0)
    tumbaF2C23 = Tumba("Tumbita El Amor Trasciende", cementerioF22Cu, 1.80, 1)
    tumbaF2C24 = Tumba("Tumbita Una Vida Lleno de Amor", cementerioF22Cu, 1.60, 1)
    tumbaF2C25 = Tumba("Tumbita Copa del Encanto", cementerioF22Cu, 1.75, 2)
    tumbaF2C26 = Tumba("Tumbita Portal de Arte", cementerioF22Cu, 1.70, 2)

    # Cementerio 3 Tumbas Cuerpos
    tumbaF2C31 = Tumba("Tumbita Esfera de Serenidad", cementerioF23Cu, 1.70, 0)
    tumbaF2C32 = Tumba("Tumbita Reflejo de Elegancia", cementerioF23Cu, 1.65, 0)
    tumbaF2C33 = Tumba("Tumbita Caja de Maravillas", cementerioF23Cu, 1.60, 1)
    tumbaF2C34 = Tumba("Tumbita Jardín del Recuerdo", cementerioF23Cu, 1.50, 1)
    tumbaF2C35 = Tumba("Tumbita Refugio del Alma", cementerioF23Cu, 1.75, 1)
    tumbaF2C36 = Tumba("Tumbita Lugar de Serenidad", cementerioF23Cu, 1.40, 2)

    # Cementerio 4 Tumbas Cuerpos
    tumbaF2C41 = Tumba("Tumbita Eterna Luz", cementerioF24Cu, 1.70, 1)
    tumbaF2C42 = Tumba("Tumbita Sombra Sagrada", cementerioF24Cu, 1.80, 0)
    tumbaF2C43 = Tumba("Tumbita Cámara del Silencio", cementerioF24Cu, 1.60, 1)
    tumbaF2C44 = Tumba("Tumbita Rincón de Paz", cementerioF24Cu, 1.80, 1)
    tumbaF2C45 = Tumba("Tumbita Hogar de Paz", cementerioF24Cu, 1.75, 2)
    tumbaF2C46 = Tumba("Tumbita Sendero de Tranquilidad", cementerioF24Cu, 1.50, 2)

    # Cementerio 5 Tumbas Cuerpos
    tumbaF2C51 = Tumba("Tumbita Velo de Recuerdo", cementerioF25Cu, 1.70, 0)
    tumbaF2C52 = Tumba("Tumbita Cascada de Paz", cementerioF25Cu, 1.70, 0)
    tumbaF2C53 = Tumba("Tumbita Refugio Perpetuo", cementerioF25Cu, 1.60, 1)
    tumbaF2C54 = Tumba("Tumbita Sombra de Amor", cementerioF25Cu, 1.65, 0)
    tumbaF2C55 = Tumba("Tumbita Eterna Quietud", cementerioF25Cu, 1.58, 2)
    tumbaF2C56 = Tumba("Tumbita Altar de Recuerdos", cementerioF25Cu, 1.68, 2)

    # Cementerio 6 Tumbas Cuerpos
    tumbaF2C61 = Tumba("Tumbita Una Vida de Amor y Bondad", cementerioF26Cu, 1.50, 0)
    tumbaF2C62 = Tumba("Tumbita Siempre en Nuestro Corazón y Pensamiento", cementerioF26Cu, 1.40, 0)
    tumbaF2C63 = Tumba("Tumbita En Tu Ausencia", cementerioF26Cu, 1.60, 1)
    tumbaF2C64 = Tumba("Tumbita Tu Presencia es Más Fuerte", cementerioF26Cu, 1.68, 1)
    tumbaF2C65 = Tumba("Tumbita Una Vida Dedicada al Amor", cementerioF26Cu, 1.75, 2)
    tumbaF2C66 = Tumba("Tumbita Un Alma Valiente", cementerioF26Cu, 1.60, 2)

    cuenta7CR = 7
    cuenta8CR = 8
    cuenta9CR = 9
    cuenta10CR = 10
    cuenta11CR = 11
    cuenta12CR = 12

    # Crematorios pertenecientes a F2 --> Funeraria 2
    crematorioF21 = Crematorio("Crematorio del Silencio", 100, cuenta7CR, "oro", None, funeraria2)
    crematorioF22 = Crematorio("Ascenso y Tranquilidad", 78, cuenta8CR, "oro", None, funeraria2)

    crematorioF23 = Crematorio("Brasa de Paz", 78, cuenta9CR, "plata", None, funeraria2)
    crematorioF24 = Crematorio("Eterna Luz Crematorio", 78, cuenta10CR, "plata", None, funeraria2)

    crematorioF25 = Crematorio("Crematorio del Renacer", 78, cuenta11CR, "bronce", None, funeraria2)
    crematorioF26 = Crematorio("Fuego y Serenidad", 78, cuenta12CR, "bronce", None, funeraria2)

    cuenta7Cl = 7
    cuenta8Cl = 8
    cuenta9Cl = 9
    cuenta10Cl = 10
    cuenta11Cl = 11
    cuenta12Cl = 12

    # Creación de clientes
    clienteF21 = Cliente("Valeria Sánchez", 231,30, cuenta7Cl, "oro", familiarG)
    clienteF22 = Cliente("Patricia Morales", 232,25, cuenta8Cl, "oro", familiarH)
    clienteF23 = Cliente("Gabriela García", 233,90, cuenta9Cl, "plata", familiarI)
    clienteF24 = Cliente("Andrés Vargas", 234,57, cuenta10Cl, "plata", familiarJ)
    clienteF25 = Cliente("Sergio Pérez", 235,35, cuenta11Cl, "bronce", familiarK)
    clienteF26 = Cliente("Luis García", 236,50, cuenta12Cl, "bronce", familiarL)

    clienteF27 = Cliente("Rafael Morales", 0,5, None, "oro", familiarEM)
    clienteF28 = Cliente("Pablo Sánchez", 0,17, None, "oro", familiarFM)

    clienteF29 = Cliente("Ana Belén Ruiz", 0,15, None, "bronce", familiarGM)
    clienteF210 = Cliente("Claudia Romero", 0,13, None, "bronce", familiarHM)


    # Agregar clientes a la funeraria
    funeraria2.agregarCliente(clienteF21)
    funeraria2.agregarCliente(clienteF22)
    funeraria2.agregarCliente(clienteF23)
    funeraria2.agregarCliente(clienteF24)
    funeraria2.agregarCliente(clienteF25)
    funeraria2.agregarCliente(clienteF26)
    funeraria2.agregarCliente(clienteF27)
    funeraria2.agregarCliente(clienteF28)
    funeraria2.agregarCliente(clienteF29)
    funeraria2.agregarCliente(clienteF210)


    #Funcionalidad Exhumacion
    cuenta39CL = 39
    cuenta40CL = 40
    cuenta41CL = 41
    cuenta42CL = 42
    cuenta43CL = 43
    cuenta44CL = 44
    cuenta45CL = 45
    cuenta46CL = 46
    cuenta47CL = 47
    cuenta48CL = 48

    # Crear objetos Cliente
    clienteF21E = Cliente("Juan Pérez", 3212, 30, cuenta39CL, "oro", familiarA)
    clienteF22E = Cliente("Carlos Fernández", 3213, 25, cuenta40CL, "oro", familiarA)

    clienteF23E = Cliente("Miguel Rodríguez", 3213, 90, cuenta41CL, "plata", familiarC)
    clienteF24E = Cliente("Dani Morales", 3214, 57, cuenta42CL, "plata", familiarC)

    clienteF25E = Cliente("Pedro González", 3215, 50, cuenta43CL, "bronce", familiarB)
    clienteF26E = Cliente("José Martínez", 3215, 30, cuenta44CL, "bronce", familiarA)

    clienteF27E = Cliente("María López", 0,5,None, "oro", familiarB)
    clienteF28E = Cliente("Carmen García", 0,17,None, "oro", familiarB)

    clienteF29E = Cliente("Ana Torres", 0,15,None, "bronce", familiarB)
    clienteF210E = Cliente("Isabel Ramírez", 0,13,None, "bronce", familiarB)

    clienteF211E = Cliente("Laura Morales", 233, 90, cuenta45CL, "plata", familiarA)
    clienteF212E = Cliente("Robert Jones", 234, 57, cuenta46CL, "plata", familiarC)

    clienteF213E = Cliente("Olivia Miller", 235, 35, cuenta47CL, "bronce", familiarC)
    clienteF214E = Cliente("Sophia Moore", 236, 50, cuenta48CL, "bronce", familiarC)

    clienteF215E = Cliente("James Smith", 0,5,None, "oro", familiarB)
    clienteF216E = Cliente("David Brown", 0,17,None, "oro", familiarB)

    clienteF217E = Cliente("John Williams", 0,15,None, "bronce", familiarB)
    clienteF218E = Cliente("Michael Johnson", 0,13,None, "bronce", familiarB)

    # Cementerio 1 Cenizas
    urnaF2C11E = Urna("Urnita de la Esperanza", cementerioF21Ce, 70, 1, "fija")
    urnaF2C12E = Urna("Urnita del Futuro", cementerioF21Ce, 80, 0, "fija")
    urnaF2C13E = Urna("default", cementerioF21Ce, 60, 0, "ordinaria")

    urnaF2C14E = Urna("Urnita de la Esperanza", cementerioF21Ce, 70, 1, "fija")
    urnaF2C15E = Urna("Urnita del Futuro", cementerioF21Ce, 80, 0, "fija")

    # Cementerio 2 Cenizas
    urnaF2C21E = Urna("Urnita de la Sabiduría", cementerioF22Ce, 70, 1, "fija")
    urnaF2C22E = Urna("Urnita de la Justicia", cementerioF22Ce, 80, 0, "ordinaria")
    urnaF2C23E = Urna("default", cementerioF22Ce, 90, 0, "fija")

    urnaF2C24E = Urna("Urnita de la Sabiduría", cementerioF22Ce, 70, 1, "fija")
    urnaF2C25E = Urna("Urnita de la Justicia", cementerioF22Ce, 80, 0, "ordinaria")

    # Cementerio 3 Cenizas
    urnaF2C31E = Urna("Urnita de la Confianza", cementerioF23Ce, 70, 1, "fija")
    urnaF2C32E = Urna("Urnita del Progreso", cementerioF23Ce, 80, 0, "fija")
    urnaF2C33E = Urna("default", cementerioF23Ce, 90, 1, "fija")

    urnaF2C34E = Urna("Urnita de la Confianza", cementerioF23Ce, 70, 1, "fija")
    urnaF2C35E = Urna("Urnita del Progreso", cementerioF23Ce, 80, 0, "fija")

    # Cementerio 4 Cenizas
    urnaF2C41E = Urna("Urnita de la Verdadera Voz", cementerioF24Ce, 70, 1, "fija")
    urnaF2C42E = Urna("Urnita de la Decisión", cementerioF24Ce, 80, 0, "fija")
    urnaF2C43E = Urna("default", cementerioF24Ce, 60, 1, "fija")

    urnaF2C44E = Urna("Urnita de la Verdadera Voz", cementerioF24Ce, 70, 1, "fija")
    urnaF2C45E = Urna("Urnita de la Decisión", cementerioF24Ce, 80, 0, "fija")

    # Cementerio 5 Cenizas
    urnaF2C51E = Urna("Urnita del Cambio", cementerioF25Ce, 70, 2, "fija")
    urnaF2C52E = Urna("Urnita del Pueblo", cementerioF25Ce, 80, 0, "fija")
    urnaF2C53E = Urna("default", cementerioF25Ce, 60, 1, "ordinaria")

    urnaF2C54E = Urna("Urnita del Cambio", cementerioF25Ce, 70, 2, "fija")
    urnaF2C55E = Urna("Urnita del Pueblo", cementerioF25Ce, 80, 0, "fija")

    # Cementerio 6 Cenizas
    urnaF2C61E = Urna("Urnita de la Transparencia", cementerioF26Ce, 70, 1, "fija")
    urnaF2C62E = Urna("Urnita del Compromiso", cementerioF26Ce, 80, 0, "fija")
    urnaF2C63E = Urna("default", cementerioF26Ce, 60, 0, "ordinaria")

    urnaF2C64E = Urna("Urnita de la Transparencia", cementerioF26Ce, 70, 1, "fija")
    urnaF2C65E = Urna("Urnita del Compromiso", cementerioF26Ce, 80, 0, "fija")

    urnaF2C11E.agregarCliente(clienteF21E)
    urnaF2C12E.agregarCliente(clienteF22E)
    urnaF2C13E.agregarCliente(clienteF23E)

    urnaF2C21E.agregarCliente(clienteF24E)
    urnaF2C22E.agregarCliente(clienteF25E)
    urnaF2C23E.agregarCliente(clienteF26E)

    urnaF2C31E.agregarCliente(clienteF27E)
    urnaF2C32E.agregarCliente(clienteF28E)
    urnaF2C33E.agregarCliente(clienteF29E)

    urnaF2C41E.agregarCliente(clienteF210E)
    urnaF2C42E.agregarCliente(clienteF211E)
    urnaF2C43E.agregarCliente(clienteF212E)

    urnaF2C51E.agregarCliente(clienteF213E)
    urnaF2C52E.agregarCliente(clienteF214E)
    urnaF2C53E.agregarCliente(clienteF215E)

    urnaF2C61E.agregarCliente(clienteF216E)
    urnaF2C62E.agregarCliente(clienteF217E)
    urnaF2C63E.agregarCliente(clienteF218E)

    cuenta49CL = ("cuenta49CL", "oro")
    cuenta50CL = ("cuenta50CL", "oro")
    cuenta51CL = ("cuenta51CL", "plata")
    cuenta52CL = ("cuenta52CL", "plata")
    cuenta53CL = ("cuenta53CL", "bronce")
    cuenta54CL = ("cuenta54CL", "bronce")

    cuenta55CL = ("cuenta55CL", "plata")
    cuenta56CL = ("cuenta56CL", "plata")
    cuenta57CL = ("cuenta57CL", "bronce")
    cuenta58CL = ("cuenta58CL", "bronce")

    # Clientes para tumbas

    clienteF21ET = Cliente("Ezequiel Andrade", 123, 30, cuenta49CL, "oro", familiarC)
    clienteF22ET = Cliente("Damián Vargas", 1234, 25, cuenta50CL, "oro", familiarC)

    clienteF23ET = Cliente("Octavio Salazar", 1235, 90, cuenta51CL, "plata", familiarB)
    clienteF24ET = Cliente("Leonardo Paredes", 1236, 57, cuenta52CL, "plata", familiarB)

    clienteF25ET = Cliente("Ulises Ortega", 1237, 21, cuenta53CL, "bronce", familiarC)
    clienteF26ET = Cliente("Valeria Castro", 1238, 50, cuenta54CL, "bronce", familiarC)

    clienteF27ET = Cliente("Delfina Méndez", 5, "oro", familiarB)
    clienteF28ET = Cliente("Mireya Delgado", 17, "oro", familiarB)

    clienteF29ET = Cliente("Renata Aguirre", 15, "plata", familiarB)
    clienteF210ET = Cliente("Alma Guzmán", 13, "plata", familiarB)

    clienteF211ET = Cliente("Leo Cruz", 1235, 90, cuenta55CL, "plata", familiarB)
    clienteF212ET = Cliente("Luna Martínez", 1236, 57, cuenta56CL, "plata", familiarB)

    clienteF213ET = Cliente("Lucas Moreno", 1237, 21, cuenta57CL, "bronce", familiarC)
    clienteF214ET = Cliente("Sofía Rodríguez", 1238, 50, cuenta58CL, "bronce", familiarC)

    # Clientes menores de edad
    clienteF215ET = Cliente("Aitana Gómez", 0,5,None, "oro", familiarB)
    clienteF216ET = Cliente("Zoe García", 0,17,None, "oro", familiarB)

    clienteF217ET = Cliente("Ethan Ortega", 0,15,None, "plata", familiarB)
    clienteF218ET = Cliente("Dylan Mendoza", 0,13,None, "plata", familiarB)

    # Cementerio 1
    tumbaF2C11E = Tumba("Tumbita Lugar de Paz", cementerioF21Cu, 1.70, 1)
    tumbaF2C12E = Tumba("Tumbita Descanso Eterno", cementerioF21Cu, 1.50, 0)
    tumbaF2C13E = Tumba("default", cementerioF21Cu, 1.60, 0)

    tumbaF2C14E = Tumba("Tumbita Lugar de Paz", cementerioF21Cu, 1.70, 1)
    tumbaF2C15E = Tumba("Tumbita Descanso Eterno", cementerioF21Cu, 1.50, 0)

    # Cementerio 2
    tumbaF2C21E = Tumba("Tumbita Siempre Recordado", cementerioF22Cu, 1.70, 1)
    tumbaF2C22E = Tumba("Tumbita En Honor a un Ser Querido", cementerioF22Cu, 1.50, 0)
    tumbaF2C23E = Tumba("default", cementerioF22Cu, 1.50, 0)

    tumbaF2C24E = Tumba("Tumbita Siempre Recordado", cementerioF22Cu, 1.70, 1)
    tumbaF2C25E = Tumba("Tumbita En Honor a un Ser Querido", cementerioF22Cu, 1.50, 0)

    # Cementerio 3
    tumbaF2C31E = Tumba("Tumbita Lugar de Serenidad", cementerioF23Cu, 1.70, 1)
    tumbaF2C32E = Tumba("Tumbita Eterna Paz", cementerioF23Cu, 1.50, 0)
    tumbaF2C33E = Tumba("default", cementerioF23Cu, 1.60, 0)

    tumbaF2C34E = Tumba("Tumbita Lugar de Serenidad", cementerioF23Cu, 1.70, 1)
    tumbaF2C35E = Tumba("Tumbita Eterna Paz", cementerioF23Cu, 1.50, 0)

    # Cementerio 4
    tumbaF2C41E = Tumba("Tumbita Un Alma Bella", cementerioF24Cu, 1.70, 1)
    tumbaF2C42E = Tumba("Tumbita En Paz y Serenidad", cementerioF24Cu, 1.50, 0)
    tumbaF2C43E = Tumba("default", cementerioF24Cu, 1.70, 0)

    tumbaF2C44E = Tumba("Tumbita Un Alma Bella", cementerioF24Cu, 1.70, 1)
    tumbaF2C45E = Tumba("Tumbita En Paz y Serenidad", cementerioF24Cu, 1.50, 0)

    # Cementerio 5
    tumbaF2C51E = Tumba("Tumbita Siempre en Nuestros Corazones", cementerioF25Cu, 1.70, 1)
    tumbaF2C52E = Tumba("Tumbita Aquí Descansa en Paz", cementerioF25Cu, 1.50, 0)
    tumbaF2C53E = Tumba("default", cementerioF25Cu, 1.90, 0)

    tumbaF2C54E = Tumba("Tumbita Siempre en Nuestros Corazones", cementerioF25Cu, 1.70, 1)
    tumbaF2C55E = Tumba("Tumbita Aquí Descansa en Paz", cementerioF25Cu, 1.50, 0)

    # Cementerio 6
    tumbaF2C61E = Tumba("Tumbita La Luz de Nuestra Vida", cementerioF26Cu, 1.70, 1)
    tumbaF2C62E = Tumba("Tumbita Aquí La Memoria Vive", cementerioF26Cu, 1.50, 0)
    tumbaF2C63E = Tumba("default", cementerioF26Cu, 1.60, 0)

    tumbaF2C64E = Tumba("Tumbita La Luz de Nuestra Vida", cementerioF26Cu, 1.70, 1)
    tumbaF2C65E = Tumba("Tumbita Aquí La Memoria Vive", cementerioF26Cu, 1.50, 0)
    
    # Cementerio 1
    tumbaF2C11E.agregarCliente(clienteF21ET)
    tumbaF2C12E.agregarCliente(clienteF22ET)
    tumbaF2C13E.agregarCliente(clienteF23ET)

    # Cementerio 2
    tumbaF2C21E.agregarCliente(clienteF24ET)
    tumbaF2C22E.agregarCliente(clienteF25ET)
    tumbaF2C23E.agregarCliente(clienteF26ET)

    # Cementerio 3
    tumbaF2C31E.agregarCliente(clienteF27ET)
    tumbaF2C32E.agregarCliente(clienteF28ET)
    tumbaF2C33E.agregarCliente(clienteF29ET)

    # Cementerio 4
    tumbaF2C41E.agregarCliente(clienteF210ET)
    tumbaF2C42E.agregarCliente(clienteF211ET)
    tumbaF2C43E.agregarCliente(clienteF212ET)

    # Cementerio 5
    tumbaF2C51E.agregarCliente(clienteF213ET)
    tumbaF2C52E.agregarCliente(clienteF214ET)
    tumbaF2C53E.agregarCliente(clienteF215ET)

    # Cementerio 6
    tumbaF2C61E.agregarCliente(clienteF216ET)
    tumbaF2C62E.agregarCliente(clienteF217ET)
    tumbaF2C63E.agregarCliente(clienteF218ET)

    ventanaInicio.ventanaInicio()


		
