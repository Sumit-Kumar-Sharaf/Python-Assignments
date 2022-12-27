# Write a python script to print first M multiples of N.
n=int(input("Enter A Number Of Which You Want To Print First n Multiples : "))
for e in range(int(input("How Many Multiples Of %d You Want : "%n))):
    print(n*(e+1),end=' ')