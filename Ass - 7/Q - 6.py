s=str(input("Enter A String : "))
match s:
    case s if " " in s:
        print("Multiword String")
    case s if " " not in s:
        print("Singleword String")