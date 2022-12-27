""" Write a recursive python function to print first N natural numbers."""
def naturalNumber(n):
    if n>0:
        naturalNumber(n-1)
        print(n,end=" ")

naturalNumber(int(input("How Many Natural Numbers Do You Want To Print ? : ")))