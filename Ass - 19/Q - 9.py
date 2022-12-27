""" Write a python program to create a function to check 
whether a number falls in a given range """

def check(r,x):
    for e in r:
        if e==x:
            print("%d Exist In Range"%x)
            break
    else:
        print("%d Do Not Exist In Range"%x)

check(range(2,20,2),16)