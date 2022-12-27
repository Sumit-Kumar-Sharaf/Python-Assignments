""" Write a python program to create a function which expects an unknown
number of arguments """

def variableLengthArgument(*t):
    print(*t,end=" ")

variableLengthArgument(10,10.5,"Sumit",True)