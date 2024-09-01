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

    