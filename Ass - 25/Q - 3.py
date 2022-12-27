""" Write a python script to update 2nd Question, change email and age to 
__email and __age """

class Profile:
    def __init__(self) -> None:
        self.name=None
        self.__email=None
        self.__age=None

    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name

    def setEmail(self,mail_id):
        self.__email=mail_id
    def getEmail(self):
        return self.__email

    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age