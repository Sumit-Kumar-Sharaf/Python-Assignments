# Write a Python script to create a list of first N natural numbers.
l=[]
num=int(input("How Many Natural NUmbers Do You Want To Print : "))
for e in range(num):
    l.append(e+1)
print(l)