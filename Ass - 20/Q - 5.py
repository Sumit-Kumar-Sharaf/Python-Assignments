""" Write a python program to create a function to find the Min of
three numbers """

def minimum(x,y,z):
    a,b,c=x,y,z
    l=[a,b,c]
    return min(l)

print("Minium Number =",minimum(126,66,77))