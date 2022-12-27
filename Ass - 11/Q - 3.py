# Write a python script to calculate sum of cubes of first N natural numbers.
sum=0
for e in range(int(input("Of First How Many Natural Numbers You Want To Print The  Sum Of Squares : "))):
    sum=sum+(e+1)**3
print(sum)