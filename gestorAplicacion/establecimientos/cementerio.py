from typing import List
from enum import Enum


from gestorAplicacion.establecimientos.establecimiento import Establecimiento
from gestorAplicacion.establecimientos.iglesia import Iglesia
from gestorAplicacion.inventario.inventario import Inventario
from gestorAplicacion.inventario.urna import Urna

class Cementerio(Establecimiento):
    cementerios= []

    def __init__(self, nombre: str, capacidad: int, cuentaCorriente, afiliacion: str, empleado, tipo: str, funeraria):
        super().__init__(nombre, capacidad, cuentaCorriente, afiliacion, empleado, funeraria)
        self._tipo = tipo
        self._inventario = []
        Cementerio.cementerios.append(self)

    @staticmethod
    def cementerioPorTipo(cementerios, tipo) -> List[Establecimiento]:
        cementeriosDisponibles = []
        for c in cementerios:
            if isinstance(c, Cementerio) and c.getTipo() == tipo:
                cementeriosDisponibles.append(c)
        return cementeriosDisponibles

    def disponibilidadInventario(self, urnaTumba, tamaño, edad):
        inventarioDisponible = []
        auxInventario=[]

        if urnaTumba=="tumba":
             auxInventario = self._inventario
        else: auxInventario=self.tipoUrna()
        
        for item in auxInventario:
            if (item.getCliente() is None and
                item.getTamaño() >= item.determinarTamaño(tamaño) and
                item.getCategoria() == item.determinarCategoria(edad)):
                inventarioDisponible.append(item)
                
        return inventarioDisponible
    
    def inventarioRecomendado(self, inventario):
        if self._inventario==[]:
            return None
        menor=inventario[0].getTamaño()
        recomendado=inventario[0]

        for i in inventario:
            if(i.getTamaño()<menor):
                menor=i.getTamaño()
                recomendado=i
       
        return recomendado


    def tipoUrna(self):
        iglesia = (self.getIglesia()).name
        if iglesia == "BUDISMO" or iglesia == "CRISTIANISMO":
            return self._inventario
        elif iglesia == "HINDUISMO":
            return self.urnasPorTipo("ordinaria")
        elif iglesia == "TAOISMO":
            return self.urnasPorTipo("fija")
        else:
            return self._inventario
    
    def inventarioDefault(self) :
        porDefecto = []
        auxInventario = self.urnasPorTipo("fija") if self._tipo == "cenizas" else self._inventario
        for item in auxInventario:
            if item.getNombre() == "default" and item.getCliente() is not None:
                porDefecto.append(item)
                
        return porDefecto


    def urnasPorTipo(self, tipo):
        urnasPorTipo = []
        for item in self._inventario:
            if isinstance(item, Urna) and item.getTipo() == tipo:
                urnasPorTipo.append(item)
        return urnasPorTipo

    def organizarIglesia(self, cliente):
        familiares = cliente.getFamiliares()
        sillas = self.getIglesia().getSillas()
        organizacion = ""
        productos = []

        cliente.getInventario().generarAdornos("flores")

        contador = 1
        while familiares and sillas:
            familiar = cliente.designarFamiliar(familiares)
            flor = cliente.getInventario().getInventarioFlores()[0]
            organizacion += f"Silla [{contador}] - Familiar {familiar} Flores para decorar silla - {flor}\n"
            productos.append({"nombre": flor, "precio": Inventario.precios(flor), "cantidad": 1})
            familiares.remove(familiar)
            cliente.getInventario().getInventarioFlores().remove(flor)
            sillas -= 1
            contador += 1
        
        cliente.agregarFactura({"productos": productos})
        return organizacion

    def agregarInventario(self, inventario: Inventario):
        self._inventario.append(inventario)

    def getTipo(self):
        return self._tipo

    def setTipo(self, tipo: str):
        self._tipo = tipo

    def getInventario(self) -> List[Inventario]:
        return self._inventario

    def setInventario(self, inventario: List[Inventario]):
        self._inventario = inventario

    @staticmethod
    def getCementerios() -> List['Cementerio']:
        return Cementerio.cementerios