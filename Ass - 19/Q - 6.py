""" Write a python program to create a function that finds a maximum
of four numbers """

def maxElement(a,b,c,d):
    p,q,r,s=a,b,c,d
    l=[p,q,r,s]
    print("Greatest Number =",max(l))

maxElement(10,3,50,6)