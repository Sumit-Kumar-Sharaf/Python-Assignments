""" Write a python program to create a function and print a list where
the values are square of numbers between 1 and 30 """

def square():
    l=[e**2 for e in range(2,30)]
    print(l)

print(square())