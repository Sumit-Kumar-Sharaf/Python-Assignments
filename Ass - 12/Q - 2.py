# Write a python script to check whether a given number is Prime or not.
n=int(input("Enter A Number : "))
for e in range(2,n):
    if n%e==0:
        print("%d Is Not A Prime Number"%n)
        break
else:
    print("%d Is A Prime Number"%n)

