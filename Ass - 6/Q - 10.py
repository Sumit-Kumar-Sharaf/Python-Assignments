# Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
num1=int(input("Enter 1st Number\n"))
num2=int(input("Enter 2nd Number\n"))
num3=int(input("Enter 3rd Number\n"))
if num1>num2:
    if num1>num3:
        print("Greater Number =",num1)
    else:
        print("Greater Number =",num3)
else:
    if num2>num3:
        print("Greater Number =",num2)
    else:
        print("Greater Number =",num3)