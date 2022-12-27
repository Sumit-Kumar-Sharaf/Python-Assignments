# Write a python script to print the first 10 multiples of N in reverse order.
n=int(input("Enter A Number Of Which You Want To Print First 10 Multiples In Reverse Order : "))
for e in range(10,0,-1):
    print(n*e,end=" ")
