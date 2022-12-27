""" Write a recursive python function to calculate sum
of cubes of first N natural numbers """

def cubeSum(n):
    if n==0:
        return 0
    return n**3+cubeSum(n-1)

res=cubeSum(int(input("Sum Of Cubes Of How Many Numbers Do You want : ")))
print(res)