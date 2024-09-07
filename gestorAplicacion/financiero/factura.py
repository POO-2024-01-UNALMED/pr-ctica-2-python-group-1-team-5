#Para que les funcione el multimethod deben poner pip install multimethod en la terminal
#from multimethod import multimethod
from datetime import datetime
from typing import List

class Factura():
    # Atributos de clase
    _IVA = 0.19
    _facturasCreadas = 0
    facturas = []
     
    #@multimethod
    def __init__(self, producto=None, precio=0, fecha=None, cliente=None, entidad=None, servicio="Inventario", lista_productos=None):
        # Atributos de instancia
        self._ID = Factura._facturasCreadas + 1
        Factura._facturasCreadas = self._ID
        self._producto = producto
        self._precio = precio
        self._total = 0
        self._cliente = cliente
        self._entidad = entidad
        self._fecha = fecha 
        self._precioFinal = 0
        self._listaProductos = lista_productos if lista_productos else []
        self._porcentajeCreditoPorPagar = 1.0
        self._servicio = servicio
        
        if not lista_productos:
            self.calcularTotal()
        else:
            self.totalFactura()

        Factura.facturas.append(self)
    #calcula el total del precio de la factura
    def totalFactura(self):
        self._total = sum(producto.getPrecio() * producto.getCantidad() for producto in self._listaProductos)
        return self._total
    
    def aplicar_descuento(self, porcentaje):
        if 0 < porcentaje <= 100:
            self._precio -= self._precio * (porcentaje / 100)
    #aplica el iva al precio total
    def calcularTotal(self):
        self._total = self._precio + (self._precio * self._IVA)

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)
        self.precio += producto.getPrecio() * producto.getCantidad()
        self.calcular_total()

    
    # Getters para atributos de clase
    @classmethod
    def getIVA(cls):
        return cls.IVA

    @classmethod
    def getFacturasCreadas(cls):
        return cls.facturas_creadas

    @classmethod
    def getFacturas(cls):
        return cls.facturas

    # Setters para atributos de clase
    @classmethod
    def setIVA(cls, IVA):
        cls.IVA = IVA

    @classmethod
    def setFacturasCreadas(cls, facturas_creadas):
        cls.facturas_creadas = facturas_creadas

    @classmethod
    def setFacturas(cls, facturas):
        cls.facturas = facturas
    
    # Getters
    def getID(self):
        return self._ID
        
    def getProducto(self):
        return self._producto

    def getPrecio(self):
        return self._precio

    def getTotal(self):
        return self._total

    def getCliente(self):
        return self._cliente

    def getEntidad(self):
        return self._entidad

    def getFecha(self):
        return self._fecha

    def getPrecioFinal(self):
        return self.precio_final

    def getListaProductos(self):
        return self._listaProductos

    def getPorcentajeCreditoPorPagar(self):
        return self._porcentajeCreditoPorPagar

    def getServicio(self):
        return self._servicio

    # Setters
    def setProducto(self, producto):
        self._producto = producto

    def setPrecio(self, precio):
        self._precio = precio

    def setTotal(self, total):
        self._total = total

    def setCliente(self, cliente):
        self._cliente = cliente

    def setEntidad(self, entidad):
        self._entidad = entidad

    def setFecha(self, fecha):
        self._fecha = fecha

    def setPrecioFinal(self, precio_final):
        self._precioFinal = precio_final

    def setListaProductos(self, lista_productos):
        self._listaProductos = lista_productos

    def setPorcentajeCreditoPorPagar(self, porcentaje_credito_por_pagar):
        self._porcentajeCreditoPorPagar = porcentaje_credito_por_pagar

    def setServicio(self, servicio):
        self._servicio = servicio