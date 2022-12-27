# Write a python script to print all Prime numbers between two given numbers (both values inclusive).
for e in range(int(input("Enter Starting Value Greater Than 1 : ")),int(input("Enter Ending Value : "))+1):
    for x in range(2,e):
        if e%x==0:
            break
    else:
        print(e,end=' ')