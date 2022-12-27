""" WRT 7th Question, create 3 Laptop objects and add them to the list
in the sorted order based on the ram size """

class Laptop:
    def __init__(self,processor,ram,storage):
        
        self.cpu=processor
        self.ram=ram
        self.hdd=storage

    def sortedList(l1,l2,l3):
        x=l1
        y=l2
        z=l3
        list=[x,y,z]

    def showCongif(self):
        print("CPU : ",self.cpu,"\nRAM : ",self.ram,"\nHDD : ",self.hdd,"\n")

L1=Laptop("intel","8 GB","256 GB")
L2=Laptop("intel","16 GB","512 GB")
L3=Laptop("AMD","32 GB","1 TB")
L1.showCongif()
L2.showCongif()
L3.showCongif()
Laptop.sortedList(L1,L2,L3)