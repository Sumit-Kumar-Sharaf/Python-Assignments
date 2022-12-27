""" Write a python script to update the Profile class with encapsulation """

class Profile:
    def __init__(self) -> None:
        self.name=None
        self.email=None
        self.age=None

    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name

    def setEmail(self,mail_id):
        self.email=mail_id
    def getEmail(self):
        return self.email

    def setAge(self,age):
        self.age=age
    def getAge(self):
        return self.age