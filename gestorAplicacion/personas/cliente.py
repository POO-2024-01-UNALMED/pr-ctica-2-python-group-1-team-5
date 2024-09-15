
from gestorAplicacion.personas.persona import Persona
from gestorAplicacion.personas.familiar import Familiar
from gestorAplicacion.inventario.producto import Producto
from gestorAplicacion.inventario.inventario import Inventario
from gestorAplicacion.financiero.factura import Factura

class Cliente(Persona):
 

    def __init__(self, nombre, cc, edad, cuentaBancaria=None, afiliacion=None, familiares=[]):
        super().__init__(nombre, cc, edad, cuentaBancaria)
        self._afiliacion = afiliacion
        self._inventario = None
        self._familiares = familiares
        self._listadoFacturas = []

   
    def cantidadFamiliares(self):
        cantidadFamiliares = len(self._familiares)
        for auxFamiliar in self._familiares:
            if auxFamiliar.getCC() != 0 and isinstance(auxFamiliar, Familiar):
                cantidadFamiliares += auxFamiliar.getAcompañantes()
        return cantidadFamiliares

    def designarFamiliar(self, familiares):
        parentescos = ["conyuge", "hijo", "padre", "hermano"]
        for parentesco in parentescos:
            for auxFamiliar in familiares:
                if isinstance(auxFamiliar, Familiar):
                    if auxFamiliar.getParentesco() == parentesco:
                        return auxFamiliar
        return None

    def agregarFactura(self, factura):
        self._listadoFacturas.append(factura)

    @staticmethod
    def familiaresPorEdad(adultoNiño, familiares):
        familiaresFiltrados = []
        for familiar in familiares:
            if familiar.getCC() == 0 and adultoNiño == "niño":
                familiaresFiltrados.append(familiar)
            elif familiar.getCC() != 0 and adultoNiño == "adulto":
                familiaresFiltrados.append(familiar)
        return familiaresFiltrados

    def pagoInmediato(self, tipoAdorno):
        if self._inventario is None:
            return "Inventario no disponible"
        
        self._inventario.generarAdornos(tipoAdorno)
        if tipoAdorno == "flores":
            arreglo = self._inventario.getInventarioFlores()
        else:
            arreglo = self._inventario.getInventarioMaterial()
        
        productos = [Producto(inventarioItem, Inventario.precios(inventarioItem), 1) for inventarioItem in arreglo]
        factura = Factura()
        factura.setListaProductos(productos)
        total = factura.totalFactura()
        
        familiaresA = list(self._familiares)
        familiarDesignado = None
        validacionPago = False
        
        while not validacionPago:
            familiarDesignado = self.designarFamiliar(familiaresA)
            if len(familiaresA) == 0 or familiarDesignado is None:
                return "No es posible hacer el cobro de la factura. No se podrán agregar adornos"
            
            if familiarDesignado.getCC() != 0 and familiarDesignado.getCuentaBancaria().getSaldo() >= total:
                familiarDesignado._cuentaBancaria.transaccionCuentaAhorros(total, 
                        self._inventario.getCementerio().getFuneraria().getCuentaAhorros())
                validacionPago = True
            else:
                familiaresA.remove(familiarDesignado)
        
        return (f"Descripción: Pago Adornos Entierro\n"
                f"Familiar: {familiarDesignado}\n"
                f"{factura.retornarFactura()}")
    
    # Métodos get y set
    def getAfiliacion(self):
        return self._afiliacion

    def setAfiliacion(self, afiliacion):
        self._afiliacion = afiliacion

    def getInventario(self):
        return self._inventario

    def setInventario(self, inventario):
        self._inventario = inventario

    def getFamiliares(self):
        return self._familiares

    def setFamiliares(self, familiares):
        self._familiares = familiares

    def getListadoFacturas(self):
        return self._listadoFacturas

    def setListadoFacturas(self, listadoFacturas):
        self._listadoFacturas = listadoFacturas