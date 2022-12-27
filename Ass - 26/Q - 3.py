""" Write a python script to create a to print the above user account
object using operator overloading (hint __str__ method) """

class UserAccount:
    def __init__(self,id,blnc):
        self.userid=id        
        self.balance=blnc
    def __str__(self):
        return str(print("UserID =",self.userid,"\nBalance =",self.balance))
U1=UserAccount(101,10000)
U2=UserAccount(102,20000)
U3=UserAccount(103,30000)
print(U1)
print(U2)
print(U3)
