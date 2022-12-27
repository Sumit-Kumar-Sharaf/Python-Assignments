""" Define a function which takes lengths of three sides of a triangle as arguments and
display the perimeter or triangle. Define and apply a decorator which checks for the
validity of the triangle on the basis of lengths of the side. This makes the perimeter to
be displayed when the triangle can exist with the given lengths of the sides """

def decor_perimeter(perimeter):
    def validation(a,b,c):
        if a+b>c and b+c>a and a+c>b:
            perimeter(a,b,c)
        else:
            print("Triangel Is Not Valid")
    return validation

@decor_perimeter
def perimeter(a,b,c):
    print("Perimeter = ",a+b+c)


x=int(input("Enter The Length Of 1st Side Of The Triangle : "))
y=int(input("Enter The Length Of 2nd Side Of The Triangle : "))
z=int(input("Enter The Length Of 3rd Side Of The Triangle : "))
perimeter(x,y,z)