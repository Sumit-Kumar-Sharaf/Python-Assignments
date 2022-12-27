# Write a python script to check whether a given pair of numbers are co-Prime numbers or not.
num1=int(input("Enter A Number : "))
count1=0
for e in range(2,num1):
    if num1%e==0:
        break
else:
    count1+=1
num2=int(input("Enter A Number : "))
count2=0
for e in range(2,num2):
    if num2%e==0:
        break
else:
    count2+=1
if count1==count2:
    print("Co-prime")
else:
    print("Not Co-prime")