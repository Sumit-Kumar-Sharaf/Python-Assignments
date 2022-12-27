""" Write a recursive python function to print first N odd natural
numbers """

def oddNumber(n):
    if n>0:
        oddNumber(n-1)
        print(2*n+1,end=' ')

oddNumber(int(input("How Many Odd Numbers Do You Want To Print ? : ")))