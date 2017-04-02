from ClientServer.Client import Client
import threading

class Server:
    connectedClients = list()
    msgBuffer = list()


    def acceptClient(self, client):
        if len(self.connectedClients) < 3:
            newClientThread = ClientThread(client)
            self.connectedClients.append(newClientThread)
            print("Server: new Client has connected")
            newClientThread.start()
            return True
        else:
            return False

    def distributeMessage(self, message):
        print("Server: recieved message \n")
        for clientThread in self.connectedClients:
            client = clientThread.client
            client.recieveMessage(message)


class ClientThread(threading.Thread):
    client = None


    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client



    def start(self):
        print("starting Thread")
        threading.Thread.start(self)


# class Connection:
#     message = None
#     client = None
#     server = None
#
#     def __init__(self, client, server):
#         self.client = client
#         self.server = server
#
#     def putMessage(self, message):
#         self.message = message
#
#     def takeMessage(self):
#         message = self.message
#         self.message = None
#         return message
