""" Write a recursive python function to calculate sum
of first N even natural numbers """

def evenSum(n):
    if n==0:
        return 0
    return 2*n+evenSum(n-1)

res=evenSum(int(input("Sum Of How Many Even Numbers Do You Want : ")))
print(res)