


class Datenbank():
    _accounts = {}

    def payin(self, name, value):
        if name in self._accounts:
            print(name + " payed " + str(value) + "Euro in")
            self._accounts[name] += value
            return value
        else:
            self.notKnownError(name)

    def withdraw(self, name, value):
        if name in self._accounts:
            print(name + " withdraw " + str(value) + "Euro")
            self._accounts[name] -= value
            return value
        else:
            self.notKnownError(name)

    def getBalance(self, name):
        if name in self._accounts:
            print(name + " checked his/her balance")
            return self._accounts[name]
        else:
            self.notKnownError(name)

    def addUser(self, name):
        if name not in self._accounts:
            self._accounts[name] = 0
            print("account created for " + name)
            print("balance of " + name + " is: " + str(self._accounts[name]))
        else:
            print(name + "already has an account here")

    def notKnownError(self, name):
        print(name + " has no account here")