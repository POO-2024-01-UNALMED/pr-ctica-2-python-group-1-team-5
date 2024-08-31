import random
from typing import List

from gestorAplicacion.inventario.inventario import Inventario

class Tumba(Inventario):
    def __init__(self, nombre, cementerio, tamaño, categoria):
        super().__init__(nombre, cementerio, tamaño, categoria)
        if cementerio.getTipo() == "cuerpos":
            cementerio.agregarInventario(self)

    def determinarTamaño(self, largo):
        # Medidas estándares en metros
        ancho = 1.20
        profundidad = 1.5

        # Tamaño en metros
        volumenTumba = ancho * profundidad * (largo + 0.5)
        return volumenTumba

    def generarAdornos(self, tipoAdorno):
        if tipoAdorno == "flores":
            if self.getCategoria() == 0:
                numero = 1
            elif self.getCategoria() == 1:
                numero = 2
            else:
                numero = 3

            arregloAuxiliar = Inventario.flores
            for arreglo in arregloAuxiliar:
                numeroAleatorio = random.randint(1, numero)
                while numeroAleatorio > 0:
                    self.getInventarioFlores().append(arreglo)
                    numeroAleatorio -= 1

        else:
            arregloAuxiliar = self._tipoMaterial()
            numeroAleatorio = random.randint(1, 4) - 1  # Para obtener un índice válido
            if 0 <= numeroAleatorio < len(arregloAuxiliar):
                self.getInventarioMaterial().append(arregloAuxiliar[numeroAleatorio])

    