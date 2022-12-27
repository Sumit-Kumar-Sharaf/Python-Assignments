""" Write a recursive python function to print cubes of first N natural numbers """

def cube(n):
    if n>0:
        cube(n-1)
        print(n**3,end=" ")

cube(int(input("Cube Of How Many Numbers Do You want To Print ? :")))