# Write a python script to print first N odd natural numbers in reverse order.
n=int(input("First How Many Odd Natural Numbers In Reverse Order You Want To Print : "))
while n>=0:
    print(2*n+1,end=' ')
    n-=1