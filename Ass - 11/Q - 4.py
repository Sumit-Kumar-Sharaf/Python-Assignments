# Write a python script to calculate sum of first N odd natural numbers.
sum=0
for e in range(int(input("Of First How Many Odd Natural Numbers You Want To Print The Sum : "))):
    sum=sum+(2*e)+1
print(sum)