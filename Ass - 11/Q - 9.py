#Write a python script to print binary equivalent of a given decimal number. (do not use bin() method).
n=int(input("Enter A Number : "))
temp=n
print(bin(n))
print("0b",end='')
while temp!=1:
    if (temp//2)%2==0:
        print("0",end='')
    else:
        print("1",end='')
    temp=temp//2
if n%2:
    print("1")
else:
    print("0")