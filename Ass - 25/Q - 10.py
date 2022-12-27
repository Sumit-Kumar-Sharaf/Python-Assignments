""" Write a python script to add the new method in SmartPhone class
which accepts Truecaller object as a parameter and call the fetch
method of Truecaller """

class Truecaller:
    def __init__(self) -> None:
        self.phonebook={}
        self.name=None
        self.number=None

    def add(self,number,name):
        self.number=number
        self.name=name
        self.phonebook[self.number]=self.name

    def fetch(self,number):
        return self.phonebook[number]

class Calculator:
    def multiplication(self,num1,num2):
        return num1*num2
    def division(self,num1,num2):
        return num1/num2

class Calculator2(Calculator):
    pass

class Phone:
    def calling(self):
        print("This Phone Supports Voice Calling And Video Calling Features")
    def sms(self):
        print("This Phone Support SMS And MMS Features")

class Smartphone(Calculator2,Phone):
    def Caller(self,Trueobject,number):
        return Trueobject.fetch(number)

t=Truecaller()
t.add(251198,"Sumit")
jio=Smartphone()
print(jio.Caller(t,251198))