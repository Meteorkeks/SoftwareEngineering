from Adapter.Roboter import *
from Adapter.Behave import *

class Roboter2Panzer(EnemyBehave):
    _robo = None

    def __init__(self, roboter: Roboter):
        self._robo = roboter

    def dodmg(self):
        self._robo.smash()

    def alarm(self):
        self._robo.noise()

    def move(self):
        self._robo.walk()

