from Adapter.Panzer import Panzer
from Adapter.Roboter import Roboter
from Adapter.Wrapper import Roboter2Panzer


panzer = Panzer()
panzer.alarm()
panzer.dodmg()
panzer.move()
print()

roboter = Roboter()
roboter.noise()
roboter.smash()
roboter.walk()
print()

p_roboter = Roboter2Panzer(Roboter())
p_roboter.alarm()
p_roboter.dodmg()
p_roboter.move()
print()

