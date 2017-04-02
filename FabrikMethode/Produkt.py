from abc import ABCMeta, abstractmethod

class Tisch(metaclass=ABCMeta):
    @abstractmethod
    def erzeugeBeine(self):
        pass

    @abstractmethod
    def erzeugePlatte(self):
        pass

    @abstractmethod
    def lakiere(self):
        pass




class HolzTisch(Tisch):
    def erzeugePlatte(self):
        print("erzeuge Holzplatte")

    def lakiere(self):
        print("lakiere klar")

    def erzeugeBeine(self):
        print("erzeuge Holzbeine")

class StahlTisch(Tisch):
    def erzeugePlatte(self):
        print("erzeuge Stahlplatte")

    def lakiere(self):
        print("lakiere nicht")

    def erzeugeBeine(self):
        print("erzeuge Stahlbeine")