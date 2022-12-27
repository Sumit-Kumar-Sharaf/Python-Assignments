s1=str(input("Enter First String : "))
s2=str(input("Enter Second String : "))
match (s1,s2):
    case (s1,s2) if s1==s2:
        print("{} And {} Are Identical".format(s1,s2))
    case (s1,s2) if s1>s2:
        print("{} Comes After {}".format(s1,s2))
    case (s1,s2) if s1<s2:
        print("{} Comes Before {}".format(s1,s2))