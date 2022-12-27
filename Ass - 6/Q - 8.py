# Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots.
a=int(input("Enter Coefficient Of x-Square (a)\n"))
b=int(input("Enter Coefficient Of x (b)\n"))
c=int(input("Enter Value Of Constant (c)\n"))
D=b*b-4*a*c
if D>0:
    print("Real And Distinct Roots")
elif D==0:
    print("Real And Equal Roots")
else:
    print("Imaginary Roots")