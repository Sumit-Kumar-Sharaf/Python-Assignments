'''Write a Python script to create a list, where 
each element of the list is a digit of agiven number.'''
n=int(input("Enter A Number : "))
l=[]
while n!=0:
    l.append(n%10)
    n=n//10
l.reverse()
print(l)