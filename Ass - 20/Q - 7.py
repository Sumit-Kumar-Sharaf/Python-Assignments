""" Write a python program to access a function inside a function """

def f2(f):
    print(f)

def f1():
    print("I Am First Function")

f2(f1())