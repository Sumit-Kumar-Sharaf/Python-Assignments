""" Write a python program to create a function that accepts a
string and calculate the number of upper case letters and lower
case letters """

def caseCount(str):
    ucount=0
    lcount=0
    for e in str:
        if 97<=ord(e)<=122:
            lcount+=1
        elif 65<=ord(e)<=90:
            ucount+=1
        else:
            pass
    return ucount,lcount

x,y=caseCount("Sumit Kumar Sharaf")
print("Upper Case Letters = %d"%x)
print("Lower Case Letters = %d"%y)