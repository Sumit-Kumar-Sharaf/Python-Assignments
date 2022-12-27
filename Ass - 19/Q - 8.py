"""Write a python program to multiply all the numbers
in a list."""
def elementProduct(l2):
    pro=1
    for e in l2:
        pro=pro*e
    return pro

l1=[1,2,3,4,5]
print("Product Of Elments =",elementProduct(l1))