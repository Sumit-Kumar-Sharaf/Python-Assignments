""" Write a recursive python function to print first N odd natural
numbers in reverse order """

def oddNumberReverse(n):
    if n>0:
        print(2*n+1,end=' ')
        oddNumberReverse(n-1)

oddNumberReverse(int(input("How Many Odd Numbers Do You Want To Print In Reverse Order? : ")))