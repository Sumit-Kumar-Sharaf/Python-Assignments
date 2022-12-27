"""" Write a recursive python function to print first 
N multiples of a given number """

def nMultiple(n,m):
    if m==0:
        return 1
    else:
        return n*nMultiple(n,m-1)
        
num=int(input("Enter A Number : "))
mul=int(input("How Many Multiples Of %d Do You Want ? : "%num))
print(nMultiple(num,mul))