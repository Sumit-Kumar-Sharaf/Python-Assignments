""" Create a generator to produce first n terms of Fibonacci series """

def fibonacciGenerator(n):
    a=-1
    b=1
    while n:
        c=a+b
        yield c
        n-=1
        a=b
        b=c

for e in fibonacciGenerator(int(input("How Many Terms Of Fibonacci Series Do You want To Print : "))):
    print(e,end=" ")