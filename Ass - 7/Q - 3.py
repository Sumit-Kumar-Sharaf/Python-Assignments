while True:
    print()
    print()
    print("a. Check whether a given set of three numbers are lengths of an isosceles triangle or not.")
    print("b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not.")
    print("c. Check whether a given set of three numbers are equilateral triangle or not.")
    print("d. Exit.")
    choice=str(input("Enter Your Choice : "))
    match choice:
        case "a":
            s1=eval(input("Enter Length Of 1st Side : "))
            s2=eval(input("Enter Length Of 2nd Side : "))
            s3=eval(input("Enter Length Of 3rd Side : "))
            if s1==s2 or s2==s3 or s3==s1:
                print(s1,",",s2,"And",s3,"Are Length Of An Isosceles Triangle")
            else:
                print(s1,",",s2,"And",s3,"Are Not The Length Of An Isosceles Triangle")
        case "b":
            s1=eval(input("Enter Length Of 1st Side : "))
            s2=eval(input("Enter Length Of 2nd Side : "))
            s3=eval(input("Enter Length Of 3rd Side : "))
            if s1**2+s2**2==s3**2 or s2**2+s3**2==s1**2 or s3**2+s1**2==s2**2:
                print(s1,",",s2,"And",s3,"Are Length Of Right Angled Triangle")
            else:
                print(s1,",",s2,"And",s3,"Are Not The Length Of A Right Angled Triangle")
        case "c":
            s1=eval(input("Enter Length Of 1st Side : "))
            s2=eval(input("Enter Length Of 2nd Side : "))
            s3=eval(input("Enter Length Of 3rd Side : "))
            if s1==s2==s3:
                print(s1,",",s2,"And",s3,"Are Length Of Equilateral Triangle")
            else:
                print(s1,",",s2,"And",s3,"Are Not The Length Of A Equilateral Triangle")
        case "d":
            exit()
        case _:
            print("Invalid Input")
    