""" Write a python program to create 2 objects of the user class and
assign different values """

class student:
    def __init__(self,n,r) -> None:
        self.name=n
        self.roll=r

s1=student("Sumit",17)
s2=student("Saroj",18)