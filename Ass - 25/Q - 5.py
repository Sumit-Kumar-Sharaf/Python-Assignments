""" Write a python script to create a Calculator class with 2 methods for adding
and subtracting 2 values """

class Calculator:
    def add(self,num1,num2):
        return num1+num2
    def substract(self,num1,num2):
        return num1-num2

c=Calculator()
print(c.add(15,20))
print(c.substract(20,15))