from FabrikMethode.Produkt import *
from abc import ABCMeta, abstractmethod

class TischBuilder(metaclass=ABCMeta):
    @abstractmethod
    def erzeugeTisch(self):
        pass

class HolzTischBuilder(TischBuilder):
    def erzeugeTisch(self):
        t = HolzTisch()
        t.erzeugeBeine()
        t.erzeugePlatte()
        t.lakiere()
        return t

class StahlTischBuilder(TischBuilder):
    def erzeugeTisch(self):
        t = StahlTisch()
        t.erzeugeBeine()
        t.erzeugePlatte()
        t.lakiere()
        return t
