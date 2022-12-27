# Write a Python script to create a list of first N odd natural numbers.
l=[]
num=int(input("How Many Odd Natural NUmbers Do You Want To Print : "))
for e in range(num):
    l.append(2*e+1)
print(l)