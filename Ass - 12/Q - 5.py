# Write a python script to find next prime number of a given number.
n=int(input("Enter A Number : "))
i=2*n
for e in range(n+1,i):
    for x in range(2,e):
        if e%x==0:
            break
    else:
        print(e)
        break