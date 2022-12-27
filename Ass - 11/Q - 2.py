# Write a python script to calculate sum of squares of first N natural numbers.
sum=0
for e in range(int(input("Of First How Many Natural Numbers You Want To Print The  Sum Of Squares : "))):
    sum=sum+(e+1)**2
print(sum)