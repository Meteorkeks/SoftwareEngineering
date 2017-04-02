from ClientServer.Server import Server
from ClientServer.Client import Client


server = Server()
frank = Client("frank")
henry = Client("henry")

frank.connectToServer(server)
henry.connectToServer(server)

frank.sendMessage("hey frank")

