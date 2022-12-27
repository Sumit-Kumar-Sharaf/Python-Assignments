""" Write a recursive python function to calculate sum
of first N natural numbers """

def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)

res=sum(int(input("Sum Of How Many Natural Numbers Do You Want To Print : ")))
print(res)