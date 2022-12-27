""" Write a recursive python function to calculate sum
of the digits of a given number """

def digitSum(n):
    if n==0:
        return 0
    return n%10+digitSum(n//10)

print(digitSum(int(input("Enter A Number To Get Sum Of Its Digit : "))))
