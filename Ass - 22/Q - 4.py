""" Write a recursive python function to calculate sum
of squares of first N natural numbers """

def squareSum(n):
    if n==0:
        return 0
    return n**2+squareSum(n-1)

res=squareSum(int(input("Sum Of Squares Of How Many Numbers Do You Want : ")))
print(res)