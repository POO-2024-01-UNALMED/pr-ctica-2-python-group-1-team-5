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

def funcionalidadFinanzas():
    funerarias= Establecimiento.filtrarEstablecimiento("funeraria")
    print("Seleccione la funeraria correspondiente")
    indice = 0
    for auxFuneraria in funerarias:
        indice += 1
        print(f"[{indice}] {auxFuneraria}")
    #Se escoge a la funeraria deseada
    indiceFuneraria = int(input("Ingrese el índice correspondi1ente: "))

    #Definir la funeraria
    funeraria = funerarias[indiceFuneraria-1]

    print("Que proceso quiere hacer ")
    print("[1] Cobro clientes")
    print("[2] Pagar facturas ")
    print("[3] Pago empleados")
    print("[4] credito")
    print("[5] reajuste de dinero")

    indiceProceso = int(input("Ingrese el índice correspondi1ente: "))

    if indiceProceso == 1:
        
        cementerios = funeraria.cementerios()
        print("Seleccione el cementerio correspondiente")
        indice1 = 0
        for cementerio in cementerios:
            indice1 += 1
            print(f"[{indice1}] {cementerio}")
    
    #Se escoge el cementerio deseada
    indiceCementerio = int(input("Ingrese el índice correspondi1ente: "))

    #Definir el cementerio
    cementerio = cementerios[indiceCementerio-1]

    clientes = cementerio.getClientes()
    indice1000 = 0

    if(len(clientes) > 0):
        for cliente in clientes:
            if(len(cliente.getListadoFacturas()) > 0):
                indice1000 += 1
                print(f"[{indice1000}] {cliente}")
    
    if(indice1000 == 0):
        print("No hay clientes con facturas por pagar")
        
    else:
        indiceCliente = int(input("Ingrese el índice del cliente: "))
        cliente = clientes[indiceCliente-1]
        funeraria.cobroServiciosClientes(cliente)
        print("Cobro de  facturas del cliente: "+ cliente.getNombre()+", realizado correctamente")




if __name__ == "__main__":

    print("Holaaaaa")

    banco1 = Banco.BBVA
    banco2 = Banco.BANCOLOMBIA
    banco3 = Banco.BANCO_OCCIDENTE
    banco4 = Banco.BANCO_BOGOTA
    banco5 = Banco.DAVIVIENDA

    cuenta1= CuentaBancaria(100203, "Eterna Paz",banco1, 0, 100000, 100000, 100000, 10000)
    cuenta2= CuentaBancaria(100564, "Camino de Luz", banco2, 0, 100000, 100000, 100000, 10000)
    cuenta3= CuentaBancaria(100233, "Recuerdos Eternos",banco3, 0, 100000, 100000, 100000, 10000)
    cuenta4= CuentaBancaria(135635, "Todas",banco4, 2030203)
    cuenta5= CuentaBancaria(104525, "Alejandro Rodríguez",banco5, 2030203)
    cuenta6= CuentaBancaria(567576, "Diego Martínez",banco1, 2030203)
    cuenta7= CuentaBancaria(145674, "Carlos Fernández",banco2, 2030203)
    cuenta8= CuentaBancaria(123424, "María González",banco3, 2030203)
    cuenta9= CuentaBancaria(175677, "Laura Fernández",banco4, 2030203)
    cuenta10= CuentaBancaria(175645, "Isabel Rodríguez",banco5, 2030203)

    #Funeraria
    funeraria1= Funeraria("Eterna Paz",cuenta1,cuenta4)
    funeraria2= Funeraria("Caminos de Luz",cuenta2,cuenta4)
    funeraria3= Funeraria("Recuerdos Eternos",cuenta3,cuenta4)

    #Clientes de la funeraria 1 mayores de edad
    clienteF11 = Cliente("Alejandro Rodríguez",123,30,cuenta5,"oro",None)
    clienteF12 = Cliente("Diego Martínez",1234,25,cuenta6,"oro",None)	
    clienteF13 = Cliente("Carlos Fernández",1235,90,cuenta7,"plata",None)
    clienteF14 = Cliente("María González",1236,57,cuenta8,"plata",None)
    clienteF15 = Cliente("Laura Fernández",1237,21,cuenta9,"bronce",None)
    clienteF16 = Cliente("Isabel Rodríguez",1238,50,cuenta10,"bronce",None)
	
		
	#Clientes F1 - Menores de edad
    clienteF17 = Cliente("Javier Gómez",5,"oro",None)
    clienteF18 = Cliente("Sofía Martínez",17,"oro",None)
    clienteF19 = Cliente("Carolina López",15,"plata",None)
    clienteF110= Cliente("Manuel López",13,"plata",None)
		
	
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

    facturas1 = Factura(None, 13233)

    cuentaF1Ce1= CuentaBancaria(104525, "Jardín de la Eternidad",banco5, 2030)
    cuentaF1Ce2= CuentaBancaria(567576, "Colina de la Paz",banco1, 20302)
    cuentaF1Ce3= CuentaBancaria(145674, "Campos de tranquilidad",banco2, 20302)
    cuentaF1Ce4= CuentaBancaria(123424, "Valle del Silencio",banco3, 20302)

    cementerioF11Ce = Cementerio("Jardín de la Eternidad", 78, cuentaF1Ce1, "oro", None, "cenizas", funeraria1)
    cementerioF12Ce = Cementerio("Colina de la Paz", 85, cuentaF1Ce2, "oro", None, "cenizas", funeraria1)

    cementerioF13Ce = Cementerio("Campos de tranquilidad", 79, cuentaF1Ce3, "plata", None, "cenizas", funeraria1)
    cementerioF14Ce = Cementerio("Valle del Silencio", 78, cuentaF1Ce4, "plata", None, "cenizas", funeraria1)
     
    cliente1000 = Cliente("Alejandro Rodríguez",123,30,cuenta5,"oro",None)
    cementerioF11Ce.getClientes().insert(0, cliente1000)
    cliente1000.agregarFactura(facturas1)

    funcionalidadFinanzas()

    