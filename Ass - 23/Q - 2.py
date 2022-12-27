""" Create a generator to produce first n odd natural
numbers """

def oddGenerator(n):
    x=1
    while n:
        yield x
        x+=2
        n-=1

for e in oddGenerator(int(input("How Many Odd Numbers Do You Want To Generate : "))):
    print(e,end=" ")