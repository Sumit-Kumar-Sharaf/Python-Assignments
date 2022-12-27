""" Write a python script to create an application like Truecaller 
where names and numbers are stored. Truecaller class will have 2
methods (1st to fetch the name of a number and 2nd to add a new entry) """

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

t=Truecaller()
t.add(251198,"Sumit")
t.add(251298,"Aman")
t.add(251195,"Shivam")
t.add(251005,"Rohit")
print(t.fetch(251195))
