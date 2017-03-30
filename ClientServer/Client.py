import threading

class Client:
    name = None
    server = None

    def __init__(self, name):
        self.name = name

    def connectToServer(self, server):
        print("connecting \n")
        while not server.acceptClient(self):
            pass

        print("connected!\n")
        self.server = server


    def sendMessage(self, message):
        self.server.distributeMessage(message)

    def recieveMessage(self, message):
        print(self.name + ": " + message + "\n")



