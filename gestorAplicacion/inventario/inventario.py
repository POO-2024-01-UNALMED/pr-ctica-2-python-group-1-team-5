from abc import ABC, abstractmethod

#from gestorAplicacion.personas.cliente import Cliente

class Inventario(ABC):
    precioFlores = 35000
    precioMateriales = 45000

    flores = ["Rosas", "Lirios", "Claveles", "Orquídeas", "Peonías"]
    material = ["Madera", "Metal", "Cerámica", "Vidrio", "Bambu", "Piedra"]

    _inventarioTotal= []

    def __init__(self, nombre, cementerio, tamaño, categoria):
        self._nombre = nombre
        self._cementerio = cementerio
        self._cliente = None
        self._tamaño = self.determinarTamaño(tamaño)
        self._categoria = self.determinarCategoria(categoria) if categoria > 2 else categoria

        self._inventarioFlores= []
        self._inventarioMaterial= []
        self._floresSeleccionadas= []
        self._materialSeleccionado = "por defecto"
        self._validacion = False

        Inventario._inventarioTotal.append(self)

    def agregarCliente(self, cliente):
        self._cliente = cliente
        self._cementerio.getClientes().append(cliente)
        cliente.setInventario(self)
        self._cementerio.getFuneraria().getClientes().remove(cliente)

    def determinarCategoria(self, edad) :
        if edad < 18:
            return 0
        elif edad >= 18 and edad < 60:
            return 1
        else:
            return 2

    @staticmethod
    def precios(adorno) :
        arregloCompleto = Inventario.flores + Inventario.material
        precio = 30000
        try:
            indice = arregloCompleto.index(adorno)
        except ValueError:
            return precio
        return precio + indice * 5000

    @abstractmethod
    def generarAdornos(self, tipoAdorno: str):
        pass

    @abstractmethod
    def determinarTamaño(self, tamaño: float) -> float:
        pass

    def setTamaño(self, tamaño):
        self._tamaño = self.determinarTamaño(tamaño)

    def contarAdorno(self, adorno, floresMaterial):
        if floresMaterial == "flores":
            return self._inventarioFlores.count(adorno)
        else:
            return self._inventarioMaterial.count(adorno)

    def precioTotal(self, cantidadF):
        return cantidadF * Inventario.getPrecioFlores() + Inventario.getPrecioMateriales()

    def agregarAdorno(self, adorno, floresMaterial):
        if floresMaterial == "flores":
            self._floresSeleccionadas.append(adorno)
            self._inventarioFlores.remove(adorno)
        else:
            self._materialSeleccionado=[]
            self._materialSeleccionado.append(adorno)
            self._inventarioMaterial.remove(adorno)
            

    def __str__(self):
        return self._nombre

    @staticmethod
    def getInventarioTotal():
        return Inventario._inventarioTotal

    def getNombre(self):
        return self._nombre

    def getCliente(self):
        return self._cliente

    def getCategoria(self):
        return self._categoria

    def setCategoria(self, categoria):
        self._categoria = categoria

    def getTamaño(self):
        return self._tamaño

    def getCementerio(self):
        return self._cementerio

    def setCementerio(self, cementerio):
        self._cementerio = cementerio

    def getFlores(self) :
        return self._inventarioFlores

    def getMaterial(self):
        return self._inventarioMaterial

    def getFloresSeleccionadas(self):
        return self._floresSeleccionadas

    def getMaterialSeleccionado(self):
        return self._materialSeleccionado

    def setMaterialSeleccionado(self, material):
        self._materialSeleccionado = material

    @staticmethod
    def getPrecioFlores():
        return Inventario.precioFlores

    @staticmethod
    def setPrecioFlores(precioFlores):
        Inventario._precioFlores = precioFlores

    @staticmethod
    def getPrecioMateriales():
        return Inventario._precioMateriales

    @staticmethod
    def setPrecioMateriales(precioMateriales):
        Inventario._precioMateriales = precioMateriales

    def getInventarioFlores(self):
        return self._inventarioFlores

    def setInventarioFlores(self, inventarioFlores):
        self._inventarioFlores = inventarioFlores

    def getInventarioMaterial(self):
        return self._inventarioMaterial

    def setInventarioMaterial(self, inventarioMaterial):
        self._inventarioMaterial = inventarioMaterial

    def setNombre(self, nombre):
        self._nombre = nombre

    def setCliente(self, cliente):
        self._cliente = cliente

    def setFloresSeleccionadas(self, floresSeleccionadas):
        self._floresSeleccionadas = floresSeleccionadas
