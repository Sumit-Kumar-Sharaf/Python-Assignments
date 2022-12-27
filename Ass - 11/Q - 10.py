# Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method).
n=int(input("Enter A Number : "))
print('0o',end='')
if 0<n<=7:
    print(n)
else :
    print(n//8,end='')
    print(n%8)