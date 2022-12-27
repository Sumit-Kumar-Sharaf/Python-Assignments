# Write a python script to print first N terms of a Fibonacci series.
num=int(input("How Many Terms Of Fibonacci Series Do You Want To Print : "))
count=0
a=-1
b=1
while True:
    c=a+b
    print(c,end=' ')
    count+=1
    if count==num:
        break
    a=b
    b=c