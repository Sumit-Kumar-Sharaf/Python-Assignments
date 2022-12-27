""" Write a recursive python function to calculate sum
of first N odd natural numbers """

def oddsum(n):
    if n==0:
        return 0
    return (2*n-1)+oddsum(n-1)

res=oddsum(int(input("Sum Of How Many Odd Numbers Do You want To Print : ")))
print(res)