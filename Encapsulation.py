class secretToLife:
    def __init__(self):
        self.__privateStr = "The secret to life is 42"

    def getPrivate(self):
        print(self.__privateStr)

    def setPrivate(self, private):
        self.__privateStr = private

obj = secretToLife()
obj.getPrivate()
obj.setPrivate("Oops, did I just say that out loud? 0_0")
obj.getPrivate()
