from enum import Enum
from typing import List, Optional
from datetime import datetime, time, timedelta

class Iglesia(Enum):
    
    HINDUISMO = {
        "nombre": "Kamakhya Temple",
        "sillas": 7,
        "cremacion": True,
        "duracionEvento": 4,
        "tipoUrna": ["ordinaria"],
        "religioso": "Pundit",
        "religiosoAltoRango": "Guru"
    }

    BUDISMO = {
        "nombre": "Templo de Nanjing",
        "sillas": 8,
        "cremacion": True,
        "duracionEvento": 3,
        "tipoUrna": ["fija", "ordinaria"],
        "religioso": "Monje budista",
        "religiosoAltoRango": "Abad"
    }

    CRISTIANISMO = {
        "nombre": "Iglesia de la Sagrada Familia",
        "sillas": 5,
        "cremacion": True,
        "duracionEvento": 1,
        "tipoUrna": ["fija", "ordinaria"],
        "religioso": "Padre",
        "religiosoAltoRango": "Obispo"
    }

    ISLAM = {
        "nombre": "Mezquita del Profeta",
        "sillas": 6,
        "cremacion": False,
        "duracionEvento": 0,
        "tipoUrna": None,
        "religioso": "Imán",
        "religiosoAltoRango": "Sheij"
    }

    JUDAISMO = {
        "nombre": "Sinagoga de la Rua",
        "sillas": 8,
        "cremacion": False,
        "duracionEvento": 0,
        "tipoUrna": None,
        "religioso": "Rabino",
        "religiosoAltoRango": "Jazan"
    }

    TAOISMO = {
        "nombre": "Templo del Valle del Jade",
        "sillas": 3,
        "cremacion": True,
        "duracionEvento": 2,
        "tipoUrna": ["fija"],
        "religioso": "Daoist",
        "religiosoAltoRango": "Dao Shi"
    }

    def duracionEvento(self,horaInicio):
        horaFinCremacion = int(horaInicio[:2])+self.getDuracionEvento()
        return horaFinCremacion
    
    def getNombre(self):
        return self.value.get("nombre")

    def getSillas(self):
        return self.value.get("sillas")

    def getCremacion(self):
        return self.value.get("cremacion")

    def getDuracionEvento(self):
        return self.value.get("duracionEvento")

    def getTipoUrna(self):
        return self.value.get("tipoUrna")

    def getReligioso(self):
        return self.value.get("religioso")

    def getReligiosoAltoRango(self):
        return self.value.get("religiosoAltoRango")