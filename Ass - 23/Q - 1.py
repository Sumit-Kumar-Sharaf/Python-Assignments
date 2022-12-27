""" Use iter and next method to access all the elements
of a given set using while loop """

s={9,6,6,1,4,5,9,1,5,6}
it=iter(s)
while True:
    print(next(it))