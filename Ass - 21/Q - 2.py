""" Write a recursive python function to print first N natural numbers
in reverse order """

def naturalNumberReverse(n):
    if n>0:
        print(n,end=" ")
        naturalNumberReverse(n-1)

naturalNumberReverse(int(input("How Many Natural Numbers Do You Want To Print In Reverse Order? : ")))