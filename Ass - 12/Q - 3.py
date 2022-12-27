# Write a python script to print all Prime numbers under 100.
for e in range(2,100):
    for x in range(2,e):
        if e%x==0:
            break
    else:
        print(e,end=' ')