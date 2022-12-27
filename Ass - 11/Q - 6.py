# Write a python script to calculate factorial of a given number.
fact=1
for e in range(int(input("Enter A Number : ")),1,-1):
    fact=fact*e
print(fact)