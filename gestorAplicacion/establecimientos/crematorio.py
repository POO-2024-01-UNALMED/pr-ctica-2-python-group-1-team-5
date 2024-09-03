import random
from datetime import time
import time

from gestorAplicacion.establecimientos.establecimiento import Establecimiento
#from gestorAplicacion.establecimientos.cementerio import Cementerio

class Crematorio(Establecimiento):
    def __init__(self, nombre, capacidad, cuentaCorriente, afiliacion, empleado, funeraria):
        super().__init__(nombre, capacidad, cuentaCorriente, afiliacion, empleado, funeraria)

    def cambiarHorarios(self, cementerios):
        
        hora_fin = self.getIglesia().duracionEvento(self.getHoraEvento())
        
        for cementerio in cementerios:
            if not cementerio.getHorarioEventos():
                random_number = random.randint(1, 3)
            
                while random_number > 0:
                    min_hour = hora_fin
                    max_hour = 23
                
                    horas = random.randint(min_hour, max_hour)
                    minutos = random.randint(0, 59)
                
                    horaGenerada = f"{horas:02d}:{minutos:02d}"
                    cementerio.horarioEventos.append(horaGenerada)
                    random_number -= 1