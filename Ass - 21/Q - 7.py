""" Write a recursive python function to print squares of first 
N natural numbers """

def square(n):
    if n>0:
        square(n-1)
        print(n**2,end=' ')

square(int(input("Square Of How Many Numbers Do You want To Print ? :")))