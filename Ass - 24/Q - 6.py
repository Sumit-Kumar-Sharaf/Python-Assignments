""" Write a python program to create 3 user objects and find the 
youngest of all """

class person:
    def __init__(self,n,a,r):
        self.name=n
        self.age=a
        self.roll=r

    def youngest(self,s2,s3):
        if self.age<s2.age:
            if self.age<s3.age:
                print("s1 is youngest")
            else:
                print("s3 is youngest")
        else:
            if s2.age<s3.age:
                print("s2 is youngest")
            else:
                print("s3 is youngest")


p1=person("Sumit",20,17)
p2=person("saroj",28,18)
p3=person("Sushil",18,16)
p1.youngest(p2,p3)