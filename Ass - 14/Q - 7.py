# Write a Python script to remove all non int values from a list.
l=["sumit",9,6,6,"Kumar",1+4j,"9",True,15.8,5,6]
temp=0
for x in range(len(l)):
    for e in l:
        if type(e)!=type(temp):
            del(l[l.index(e)])
print(l)