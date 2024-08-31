from enum import Enum
from typing import List, Optional
from datetime import datetime, time, timedelta

class Iglesia(Enum):
    Hinduismo = ("Kamakhya Temple", 7, True, 4, ["ordinaria"], "Pundit", "Guru")
    Budismo = ("Templo de Nanjing", 8, True, 3, ["fija", "ordinaria"], "Monje budista", "Abad")
    Cristianismo = ("Iglesia de la Sagrada Familia", 5, True, 1, ["fija", "ordinaria"], "Padre", "Obispo")
    Islam = ("Mezquita del Profeta", 6, False, 0, None, "Imán", "Sheij")
    Judaísmo = ("Sinagoga de la Rua", 8, False, 0, None, "Rabino", "Jazan")
    Taoísmo = ("Templo del Valle del Jade", 3, True, 2, ["fija"], "Daoist", "Dao Shi")

    def __init__(self, nombre: str, sillas: int, cremacion: bool, duracionEvento: int, tipoUrnas: Optional[List[str]], religioso: str, religiosoAltoRango: str):
        self._nombre = nombre
        self._sillas = sillas
        self._cremacion = cremacion
        self._duracionEvento = duracionEvento
        self._tipoUrnas = tipoUrnas if tipoUrnas is not None else []
        self._religioso = religioso
        self._religiosoAltoRango = religiosoAltoRango

    @property
    def nombre(self):
        return self._nombre

    @property
    def sillas(self):
        return self._sillas

    @property
    def cremacion(self):
        return self._cremacion

    @property
    def duracionEvento(self):
        return self._duracionEvento

    @property
    def tipoUrnas(self):
        return self._tipoUrnas

    @property
    def religioso(self):
        return self._religioso

    @property
    def religiosoAltoRango(self):
        return self._religiosoAltoRango

    def getDuracionCremacion(self):
        return self.duracionEvento

    def duracionEventoEnd(self, horaInicio: time) -> time:
        """Calcula la hora de finalización del evento a partir de la hora de inicio."""
        horaInicioDt = datetime.combine(datetime.today(), horaInicio)
        horaFinEventoDt = horaInicioDt + timedelta(hours=self.duracionEvento)
        return horaFinEventoDt.time()

    def setDuracionEvento(self, duracionEvento: int):
        self._duracionEvento = duracionEvento

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def setSillas(self, sillas: int):
        self._sillas = sillas

    def setCremacion(self, cremacion: bool):
        self._cremacion = cremacion

    def setTipoUrnas(self, tipoUrnas: Optional[List[str]]):
        self._tipoUrnas = tipoUrnas if tipoUrnas is not None else []

    def setReligioso(self, religioso: str):
        self._religioso = religioso

    def setReligiosoAltoRango(self, religiosoAltoRango: str):
        self._religiosoAltoRango = religiosoAltoRango