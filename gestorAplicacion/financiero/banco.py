from enum import Enum

class Banco(Enum):

    BANCOLOMBIA = 0.0005, 1800
    DAVIVIENDA = 0.08, 2000
    BBVA = 0.005, 1500
    BANCO_BOGOTA =  0.0001, 1600
    BANCO_OCCIDENTE = 0.02, 2200

    def __init__(self, INTERES, COBRO_ADICIONAL):
        self.INTERES = INTERES
        self.COBRO_ADICIONAL = COBRO_ADICIONAL
