age=int(input("Enter Your Age\n"))
match age:
    case age if 0<age<10:
        print("Kid")
    case age if 10<=age<20:
        print("Teen")
    case age if 20<=age<40:
        print("Young")
    case age if 40<=age<60:
        print("Experianced")
    case age if age>=60:
        print("Experianced")
    