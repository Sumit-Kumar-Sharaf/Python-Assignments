""" Create a generator to produce squares of first N natural numbers """

def squareGenerator(n):
    x=1
    while n:
        yield x**2
        x+=1
        n-=1

for e in squareGenerator(int(input("Square Of How Many Natural Numbers Do You Want To Generate : "))):
    print(e,end=" ")