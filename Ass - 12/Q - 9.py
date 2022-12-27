# Write a python script to calculate LCM of two numbers.
num1=int(input("Enter A Number : "))
num2=int(input("Enter A Number : "))
for e in range(1,(num1*num2)+1):
    if e%num1==0 and e%num2==0:
        print("LCM =",e)
        break