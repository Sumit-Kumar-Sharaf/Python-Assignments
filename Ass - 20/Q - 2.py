""" Write a python program to create a function that
takes a number as a parameter and checks if the number
is prime or not """
def isPrime(x):
    for e in range(2,x):
        if(x%e==0):
            print("%d Is Not A Prime Number"%x)
            break
    else:
        print("%d Is A Prime Number"%x)
        
isPrime(15)