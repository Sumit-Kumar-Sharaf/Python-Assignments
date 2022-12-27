""" Write a python script to join 2 threads after printing completing
the first Question """

from threading import *
def odd():
    for i in range(1,100,2):
        print(i)

def even():
    for i in range(2,101,2):
        print(i)

T1=Thread(target=odd)
T2=Thread(target=even)
T1.start()
T1.join()
T2.start()