""" Define a function which calculates HCF of two numbers. Define and apply a
decorator to check whether two given numbers are co-prime or not """

def decor_HCF(hcf):
    def coprime(a,b):
        sn=a if a<b else b
        while sn!=1:
            if a%sn==0 and b%sn==0:
                print("Not Co-prime Numbers")
                break
            sn-=1
        else:
            print("Co-prime Numbers")
        hcf(a,b)
    return coprime

@decor_HCF
def HCF(a,b):
    sn=a if a<b else b
    while sn!=1:
        if a%sn==0 and b%sn==0:
            print("HCF = ",sn)
            break
        sn-=1
    else:
        print("HCF = 1")

x=int(input("Enter 1st Number : "))
y=int(input("Enter 2nd Number : "))
HCF(x,y)
