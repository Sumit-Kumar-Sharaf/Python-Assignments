""" Create an endless iterator using generator method to produce Prime numbers """

def primeGenerator():
    for j in range(2,10**10,1):
        for i in range(2,j,1):
            if j%i==0:
                break
        else:
            yield j

it=primeGenerator()
print(next(it))
while True:
    ans=input("Do You Want To Print Next Prime NUmber ? [y/n] : ")
    if ans=="y":
        print(next(it))
    else:
        break