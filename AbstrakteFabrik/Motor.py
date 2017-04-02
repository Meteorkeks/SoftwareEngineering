from abc import ABCMeta, abstractmethod

class Motor(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

class VerbrennerMotor(Motor):
    def __init__(self):
        print("VerbrennugsMotor erzeugt")


class ElektroMototor(Motor):
    def __init__(self):
        print("ElektroMotor erzeugt")

