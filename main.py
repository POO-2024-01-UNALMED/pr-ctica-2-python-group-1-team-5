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
    print(cliente)

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
        
    print(crematorio)
        

    

if __name__ == "__main__":
    
    #Funerarias
    funeraria1= Funeraria("Eterna Paz",None,None)
    funeraria2= Funeraria("Caminos de Luz",None,None)
    funeraria3= Funeraria("Recuerdos Eternos",None,None)

    #Clientes de la funeraria 1 mayores de edad
    clienteF11 = Cliente("Alejandro Rodríguez",123,30,None,"oro",None)
    clienteF12 = Cliente("Diego Martínez",1234,25,None,"oro",None)	
    clienteF13 = Cliente("Carlos Fernández",1235,90,None,"plata",None)
    clienteF14 = Cliente("María González",1236,57,None,"plata",None)
    clienteF15 = Cliente("Laura Fernández",1237,21,None,"bronce",None)
    clienteF16 = Cliente("Isabel Rodríguez",1238,50,None,"bronce",None)
	
		
	#Clientes F1 - Menores de edad
    clienteF17 = Cliente("Javier Gómez",0,5,None,"oro",None)
    clienteF18 = Cliente("Sofía Martínez",0,17,None,"oro",None)
    clienteF19 = Cliente("Carolina López",0,15,None,"plata",None)
    clienteF110= Cliente("Manuel López",0,13,None,"plata",None)
		
	
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
		
