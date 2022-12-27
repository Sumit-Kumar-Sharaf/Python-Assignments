"""Write a python script to display all prime numbers within a range.
# range
start = 15
end = 45"""
for e in range(15,45):
    for x in range(2,e):
        if e%x==0:
            break
    else:
        print(e,end=" ")