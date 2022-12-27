# Write a python script to check whether a given number is a three digit number or not.
num=int(input("Enter A Number\n"))
temp1=num//10
temp2=temp1//10
temp3=temp2//10
if temp1!=0 and temp2!=0 and temp3==0:
    print("3 Digit Number")
else:
    print("Not A 3 Digit Number")