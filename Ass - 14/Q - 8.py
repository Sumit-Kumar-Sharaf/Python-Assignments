'''Write a Python script to print distinct elements along 
with their frequencies of occurrence in the list.'''
l=[9,6,6,1,4,5,9,1,5,6]
temp=0
for e in range(len(l)):
    for x in range(e,len(l)):
        if l[x]=="\0":
            e+=1
        else:
            print(l[e],l.count(l[e]))
            