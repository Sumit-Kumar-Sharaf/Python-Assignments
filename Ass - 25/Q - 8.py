""" Write a python script to create a SmartPhone class by inheriting 
Calculator 2.0 and Phone Class """

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
    pass

jiophone=Smartphone()
print(jiophone.multiplication(10,5))
print(jiophone.calling())