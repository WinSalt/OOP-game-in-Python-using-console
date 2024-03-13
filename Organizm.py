from abc import ABC
import COORDINATES

class Organizm(ABC):
    _sila = int()
    _inicjatywa = int()
    _wiek = int()
    _znak = int()
    _step = int()
    _wykonalRuch = bool()
    _pozycja = COORDINATES()
    #Swiat swiat;

    def _NormalnaKolizja(self):

