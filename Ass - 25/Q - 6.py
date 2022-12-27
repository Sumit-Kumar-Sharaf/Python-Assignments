""" Write a python script to create a Calculator 2.0 class with 2 methods 
for multiplication and division of 2 values and inherit it from the
Calculator class """

class Calculator:
    def multiplication(self,num1,num2):
        return num1*num2
    def division(self,num1,num2):
        return num1/num2

class Calculator2(Calculator):
    pass

c=Calculator2()
print(c.multiplication(10,2))
print(c.division(10,2))