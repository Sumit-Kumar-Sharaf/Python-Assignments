num=int(input("Enter A Number : "))
match num:
    case num if num%2==0:
        print("Saurabh Shukla")
    case num if num%2!=0 and num<0:
        print("Prateek Jain")
    case num if num%2!=0 and num>0:
        print("Prateek Jain")