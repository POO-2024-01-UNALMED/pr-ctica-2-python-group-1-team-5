from datetime import datetime
from typing import List

class Factura():
    # Atributos de clase
    IVA = 0.19
    facturas_creadas = 0
    facturas = []

    def __init__(self, producto=None, precio=0, fecha=None, cliente=None, entidad=None, servicio="Inventario", lista_productos=None):
        # Atributos de instancia
        self.ID = Factura.facturas_creadas + 1
        Factura.facturas_creadas = self.ID
        self.producto = producto
        self.precio = precio
        self.total = 0
        self.cliente = cliente
        self.entidad = entidad
        self.fecha = fecha 
        self.precio_final = 0
        self.lista_productos = lista_productos if lista_productos else []
        self.porcentaje_credito_por_pagar = 1.0
        self.servicio = servicio
        
        if not lista_productos:
            self.calcular_total()
        else:
            self.ajustar_productos()
            self.total_factura()

        Factura.facturas.append(self)
    #calcula el total del precio de la factura
    def total_factura(self):
        self.total = sum(producto.precio * producto.cantidad for producto in self.lista_productos)
        return self.total
    
    def aplicar_descuento(self, porcentaje):
        if 0 < porcentaje <= 100:
            self.precio -= self.precio * (porcentaje / 100)
    #aplica el iva al precio total
    def calcular_total(self):
        self.total = self.precio + (self.precio * self.IVA)

    
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
    def getProducto(self):
        return self.producto

    def getPrecio(self):
        return self.precio

    def getTotal(self):
        return self.total

    def getCliente(self):
        return self.cliente

    def getEntidad(self):
        return self.entidad

    def getFecha(self):
        return self.fecha

    def getPrecioFinal(self):
        return self.precio_final

    def getListaProductos(self):
        return self.lista_productos

    def getPorcentajeCreditoPorPagar(self):
        return self.porcentaje_credito_por_pagar

    def getServicio(self):
        return self.servicio

    # Setters
    def setProducto(self, producto):
        self.producto = producto

    def setPrecio(self, precio):
        self.precio = precio

    def setTotal(self, total):
        self.total = total

    def setCliente(self, cliente):
        self.cliente = cliente

    def setEntidad(self, entidad):
        self.entidad = entidad

    def setFecha(self, fecha):
        self.fecha = fecha

    def setPrecioFinal(self, precio_final):
        self.precio_final = precio_final

    def setListaProductos(self, lista_productos):
        self.lista_productos = lista_productos

    def setPorcentajeCreditoPorPagar(self, porcentaje_credito_por_pagar):
        self.porcentaje_credito_por_pagar = porcentaje_credito_por_pagar

    def setServicio(self, servicio):
        self.servicio = servicio