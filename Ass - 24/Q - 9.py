""" Write a python program to create a School class and 3 instance variable
and 1 class variable """

class School:
    Class="10th"
    def __init__(self,name,roll,section) -> None:
        self.Name=name
        self.Roll_No=roll
        self.Section=section

    def studentDetail(self):
        print("Class : ",School.Class,"\nName : ",self.Name,"\nRoll No. : ",self.Roll_No,"\nSection : ",self.Section,"\n")

s1=School("Sumit",17,"A")
s1.studentDetail()