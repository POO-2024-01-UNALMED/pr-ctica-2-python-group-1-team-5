import random
from gestorAplicacion.inventario.inventario import Inventario

class Urna(Inventario):
    def __init__(self, nombre, cementerio, peso, categoria, tipo):
        super().__init__(nombre, cementerio, peso, categoria)
        self._tipo = tipo
        self._floresUrna= []
        self._materialUrna= []

        if cementerio.getTipo() == "cenizas":
            cementerio.agregarInventario(self)

    def generarAdornos(self, tipoAdorno):
        floresUrnas = Inventario.flores
        if tipoAdorno == "flores":
            arregloAuxiliar = floresUrnas
            validacion = len(self.getFlores()) == 0
        else:
            arregloAuxiliar = self._tipoMaterial()
            validacion = len(self.getMaterial()) == 0

        if validacion:
            for arreglo in arregloAuxiliar:
                numeroAleatorio = random.randint(1, 2)
                while numeroAleatorio > 0:
                    if tipoAdorno == "flores":
                        self.getFlores().append(arreglo)
                    else:
                        self.getMaterial().append(arreglo)
                    numeroAleatorio -= 1

    def determinarTamaño(self, peso):
        tamañoBase = 16.4
        volumenNecesario = tamañoBase * peso
        return volumenNecesario

    def tipoMaterial(self):
        material = ["Madera", "Metal", "Cerámica"]
        if self._tipo == "fija":
            materialAux = ["Vidrio", "Bambu", "Piedra"]
            return materialAux
        return material

    def determinarCategoria(self, numAdornos):
        if numAdornos == 1:
            return 1
        elif numAdornos == 2:
            return 2
        return 0

    def __str__(self):
        return f"{self.getNombre()} de tipo {self._tipo}"

    def getTipo(self):
        return self._tipo

    def getFloresUrna(self):
        return self._floresUrna

    def setFloresUrna(self, floresUrna):
        self._floresUrna = floresUrna

    def getMaterialUrna(self):
        return self._materialUrna

    def setMaterialUrna(self, materialUrna):
        self._materialUrna = materialUrna

    def setTipo(self, tipo):
        self._tipo = tipo