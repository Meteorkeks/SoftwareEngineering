from abc import ABCMeta, abstractmethod

class Speicher(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

class Tank(Speicher):
    def __init__(self):
        print("Tanke erzeugt")


class Batterie(Speicher):
    def __init__(self):
        print("Batterie erzeugt")