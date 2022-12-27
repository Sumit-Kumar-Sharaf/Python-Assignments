""" Write a python program to create a function that
takes a list and returns a new list with the original
list's unique elements """

def uniqueElement(l2):
    return list(set(l2))

l1=[9,6,6,1,4,5,9,1,5,6]
print(uniqueElement(l1))