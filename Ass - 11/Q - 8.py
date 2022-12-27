# Write a python script to calculate sum of digits of a given number.
n=int(input("Enter A Number : "))
sum=0
while n!=0:
    sum=sum+n%10
    n=n//10
print("Sum Of Digits = ",sum)