""" Write a recursive python function to print first N even natural numbers
in reverse order """

def evenNumberReverse(n):
    if n>0:
        print(2*n,end=" ")
        evenNumberReverse(n-1)

evenNumberReverse(int(input("How Many Even Numbers Do You want To Print In reverse Order ? :")))