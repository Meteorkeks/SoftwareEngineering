
from Adapter.Behave import *

class Panzer(EnemyBehave):
    def dodmg(self):
        print("Shoot for 4dmg")

    def alarm(self):
        print("use Panzerhorn")

    def move(self):
        print("roll 2 fields")