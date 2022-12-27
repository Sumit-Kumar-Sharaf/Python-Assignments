# Write a python script to print first N prime numbers.
n=int(input("How Many Prime Numbers Do You Want To Print : "))
i=10*n
count=0
for e in range(2,i):
    for x in range(2,e):
        if e%x==0:
            break
    else:
        print(e,end=" ")
        count+=1
        if count==n:
            break