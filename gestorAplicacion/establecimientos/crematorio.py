import random
from datetime import time
import time

from gestorAplicacion.establecimientos.establecimiento import Establecimiento
from gestorAplicacion.establecimientos.cementerio import Cementerio

class Crematorio(Establecimiento):
    def __init__(self, nombre, capacidad, cuenta_corriente, afiliacion, empleado, funeraria):
        super().__init__(nombre, capacidad, cuenta_corriente, afiliacion, empleado, funeraria)

    def cambiarHorarios(self, cementerios):
        hora_fin = self.getIglesia().duracion_evento(self.get_hora_evento())
        
        for cementerio in cementerios:
            random_number = random.randint(1, 3)
            
            while random_number > 0:
                min_hour = hora_fin.hour
                max_hour = 23
                
                horas = random.randint(min_hour, max_hour)
                minutos = random.randint(0, 59)
                
                hora_generada = time(hour=horas, minute=minutos)
                cementerio.horarioEventos.append(hora_generada)
                random_number -= 1