""" Write a python program to create a function which expects
kwargs arguments """

def kwargsArgumnet(**dic):
    for k,v in dic.items():
        print(k,v,sep=" ")

kwargsArgumnet(Name="Sumit",Roll=17,Marks=999.99)