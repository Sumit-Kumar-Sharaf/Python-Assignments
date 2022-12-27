""" Create a generator to produce first n prime numbers """

def primeGenerator(n):
    count=0
    for j in range(2,n**2):
        for i in range(2,j):
            if j%i==0:
                break
        else:
            yield j
            count+=1
        if count==n:
            break

for e in primeGenerator(int(input("How Many Prime Numbers Do You Want To Print ? "))):
    print(e,end=" ")