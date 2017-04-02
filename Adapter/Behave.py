from abc import ABCMeta, abstractmethod

class EnemyBehave(metaclass=ABCMeta):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def alarm(self):
        pass

    @abstractmethod
    def dodmg(self):
        pass