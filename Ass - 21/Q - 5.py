""" Write a recursive python function to print first N even natural numbers """

def evenNumber(n):
    if n>0:
        evenNumber(n-1)
        print(2*n,end=" ")

evenNumber(int(input("How Many Even Numbers Do You Want To Print ? : ")))