from abc import ABCMeta, abstractmethod
from AbstrakteFabrik.Motor import *
from AbstrakteFabrik.Speicher import *

class AutoFabrik(metaclass=ABCMeta):
    @abstractmethod
    def erzeugeAuto(self):
        pass

class ElektroAutoFabrik(AutoFabrik):
    def erzeugeAuto(self):
        motor = ElektroMototor()
        speicher = Batterie()

class VerbrennerAutoFabrik(AutoFabrik):
    def erzeugeAuto(self):
        speicher = Tank()
        motor = VerbrennerMotor()

