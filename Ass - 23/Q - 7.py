""" Create an endless iterator using generator method to produce terms of
Fibonacci series """

def fibonacciGenerator():
    a,b=-1,1
    while True:
        c=a+b
        yield c
        a,b=b,c

it=fibonacciGenerator()
print(next(it))
while True:
    ans=input("Do You Want To Print Next Term ? [y/n] : ")
    if ans=="y":
        print(next(it))
    else:
        break