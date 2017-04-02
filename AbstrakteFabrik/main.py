from AbstrakteFabrik.Motor import *
from AbstrakteFabrik.Speicher import *
from AbstrakteFabrik.AutoFabrik import *

EAutoFabrik = ElektroAutoFabrik()
VAutoFabrik = VerbrennerAutoFabrik()

EAutoFabrik.erzeugeAuto()
print()
VAutoFabrik.erzeugeAuto()

