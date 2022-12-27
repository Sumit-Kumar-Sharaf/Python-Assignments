'''Write a python program to check if all items in the 
tuple are the same.'''
t=(12,12.6,12+6j,"Sumit",True)
count=0
for e in range(count,len(t)):
    for x in range((count+1),len(t)):
        if t[e]!=t[x]:
            print("False")
            break
