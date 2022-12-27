""" Create a generator to produce first n even natural numbers """

def evenGenerator(n):
    x=2
    while n:
        yield x
        x+=2
        n-=1

for e in evenGenerator(int(input("How Many Even Numbers Do You Want To Generate : "))):
    print(e,end=" ")