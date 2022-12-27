# Write a python script to calculate HCF of two numbers.
num1=int(input("Enter A Number : "))
num2=int(input("Enter A Number : "))
if num1<num2:
    small_num=num1
else:
    small_num=num2
for e in range(small_num,0,-1):
    if num1%e==0 and num2%e==0:
        print("HCF =",e)
        break
