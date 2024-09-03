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

from gestorAplicacion.inventario.urna import Urna
from gestorAplicacion.inventario.tumba import Tumba
from gestorAplicacion.inventario.producto import Producto

def funcionalidadCrematorio():

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

    #Cuentas crematorio Funeraria 1

    #Crematorio Funeraria 1
    crematorioF21 = Crematorio("Crematorio del Silencio", 100, None, "oro", None, funeraria1)
    crematorioF22 = Crematorio("Ascenso y Tranquilidad", 78, None, "oro", None, funeraria1)

    crematorioF23 = Crematorio("Brasa de Paz", 78, None, "plata", None, funeraria1)
    crematorioF24 = Crematorio("Eterna Luz Crematorio", 78, None, "plata", None, funeraria1)

    crematorioF25 = Crematorio("Crematorio del Renacer", 78, None, "bronce", None, funeraria1)
    crematorioF26 = Crematorio("Fuego y Serenidad", 78, None, "bronce", None, funeraria1)

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
    
   
    funcionalidadCrematorio()
		
