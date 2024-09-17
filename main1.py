from gestorAplicacion.establecimientos.establecimiento import Establecimiento
from gestorAplicacion.establecimientos.cementerio import Cementerio
from gestorAplicacion.establecimientos.crematorio import Crematorio
from gestorAplicacion.establecimientos.funeraria import Funeraria
from gestorAplicacion.establecimientos.iglesia import Iglesia

from gestorAplicacion.financiero.banco import Banco
from gestorAplicacion.financiero.cuentaBancaria import CuentaBancaria
from gestorAplicacion.financiero.factura import Factura

from gestorAplicacion.personas.persona import Persona
from gestorAplicacion.personas.cliente import Cliente
from gestorAplicacion.personas.empleado import Empleado
from gestorAplicacion.personas.familiar import Familiar

from gestorAplicacion.inventario.inventario import Inventario
from gestorAplicacion.inventario.urna import Urna
from gestorAplicacion.inventario.tumba import Tumba
from gestorAplicacion.inventario.producto import Producto
from gestorAplicacion.inventario.tipoVehiculo import TipoVehiculo
from gestorAplicacion.inventario.vehiculo import Vehiculo

from iuMain.funcionalidades import cremacion
from iuMain.funcionalidades import exhumacion
from iuMain import ventanaInicio

import pickle

if __name__ == "__main__":

    portafolio = open("baseDatos/objetos","rb")
    objetos1 = pickle.load(portafolio)
    portafolio.close()
    
    for sublist in objetos1:
        for item in sublist:
            if isinstance(item,Establecimiento):
                Establecimiento._establecimientos.append(item)
    
    ventanaInicio.ventanaInicio()

    portafolio = open("baseDatos/objetos","wb")
    objetos = pickle.dump(objetos1,portafolio)
    portafolio.close()
		


		
