

from Datenbank import *
from Client import *



DB = Datenbank()

client1 = Client("tick")
client2 = Client("trick")
client3 = Client("track")

client1.register(DB)
client2.register(DB)
client3.register(DB)

client1.payin(DB, 100)
client1.payin(DB, 200)
client1.withdraw(DB, 300)

