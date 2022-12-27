print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
choice=int(input("Enter Your Choice\n"))
match choice:
    case 1:
        num1=eval(input("Enter 1st Number\n"))
        num2=eval(input("Enter 2nd Number\n"))
        print("Sum =",format(num1*num2,".2f"))
    case 2:
        num1=eval(input("Enter 1st Number\n"))
        num2=eval(input("Enter 2nd Number\n"))
        print("Difference =",format(num1-num2,".2f"))
    case 3:
        num1=eval(input("Enter 1st Number\n"))
        num2=eval(input("Enter 2nd Number\n"))
        print("Product =",format(num1*num2,".2f"))
    case 4:
        num1=eval(input("Enter 1st Number\n"))
        num2=eval(input("Enter 2nd Number\n"))
        print("Quotient =",format(num1/num2,".2f"))
    case _:
        print("Invalid Choice")
    