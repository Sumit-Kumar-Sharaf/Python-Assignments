# Write a python script to count digits in a given number.
from tempfile import tempdir


count=0
n=int(input("Enter A Number Except 0 : "))
while n!=0:
    n=n//10
    count+=1
print(count)