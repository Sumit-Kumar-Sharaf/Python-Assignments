""" Write a python script to create a user account class with 2 instance variables (userid
and balance). Create 3 user objects and add all the users using operator
overloading """

class UserAccount:
    def __init__(self,id,blnc) -> None:
        self.userid=id        
        self.balance=blnc
    def __add__(self,u1=None,u2=None):
        if u2==None:
            return self.balance+u1.balance
        else:
            return self.balance+u1.balance+u2.balance

U1=UserAccount(101,10000)
U2=UserAccount(102,20000)
U3=UserAccount(103,30000)
print(U1.__add__(U2))
print(U1.__add__(U2,U3))