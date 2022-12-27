""" Write a python program to create a Laptop class with 4 attributes
(brand, ram, cpu,hdd) and 2 methods (showConfig() to print the values,
__init__() to initialize thevalues) """

class Laptop:
    
    def __init__(self,company,processor,ram,storage) -> None:
        self.brand=company
        self.cpu=processor
        self.ram=ram
        self.hdd=storage

    def showCongif(self):
        print("Brand : ",self.brand,"\nCPU : ",self.cpu,"\nRAM : ",self.ram,"\nHDD : ",self.hdd,"\n")

L1=Laptop("HP","intel i7","8 GB","500 GB")
L2=Laptop("Dell","intel i9","16 GB","1 TB")
L1.showCongif()
L2.showCongif()