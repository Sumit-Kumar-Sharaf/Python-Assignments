# Write a python script to check whether a given year is a leap year or not.
year=int(input("Enter Year\n"))
if year%100:
    if year%4:
        print("Not A Leap Year")
    else:
        print("Leap Year")
else:
    if year%400:
        print("Not A Leap Year")
    else:
        print("Leap Year")