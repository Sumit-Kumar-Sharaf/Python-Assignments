""" Write a python script to multiple 2 or 3 or 4 numbers with
a single multiply method in a class using method overloading """

class Calculator:
    def __init__(self,n1=None,n2=None,n3=None,n4=None) -> None:
        self.num1=n1
        self.num2=n2
        self.num3=n3
        self.num4=n4
    def __mul__(self):
        if self.num3==None and self.num4==None:
            return self.num1*self.num2
        elif self.num4==None:
            return self.num1*self.num2*self.num3
        else:
            return self.num1*self.num2*self.num3*self.num4

C1=Calculator(2,3)
C2=Calculator(2,3,4)
C3=Calculator(2,3,4,5)
print(C1.__mul__())
print(C2.__mul__())
print(C3.__mul__())