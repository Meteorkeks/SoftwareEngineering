from FabrikMethode.Produkt import *
from FabrikMethode.Builder import *

holzbuilder = HolzTischBuilder()
holztisch = holzbuilder.erzeugeTisch()
stahlbuilder = StahlTischBuilder()
stahltisch = stahlbuilder.erzeugeTisch()