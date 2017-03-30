
from Datenbank import Datenbank

class Client():

    cash = 0
    name = ""

    def __init__(self, name, cash = 0):
        self.name = name
        self.cash = cash

    def withdraw(self, DB, value):
        self.cash += DB.withdraw(self.name, value)


    def payin(self, DB, value):
        self.cash -= DB.payin(self.name, value)

    def register(self, DB):
        DB.addUser(self.name)
