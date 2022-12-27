"""Write a python program to merge two python dictionaries into one
dictionary"""

d1={16:"Sushil",17:"Sumit",18:"Saroj"}
d2={26:"Ajay",27:"Shuham",28:"Irshad"}
for k in d2:
    d1[k]=d2[k]
print(d1)