""" Write a python program to create a function to check
whether a given number is even or odd """

def isEven(x):
    if(x%2):
        print("%d Is A Odd Number"%x)
    else:
        print("%d Is A Even Number"%x)

isEven(int(input("Enter A Number : ")))