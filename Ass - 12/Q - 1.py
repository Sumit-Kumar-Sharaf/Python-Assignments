# Write a python script to reverse a number.
n=int(input("Enter A Number : "))
while n!=0:
    print(n%10,end='')
    n=n//10