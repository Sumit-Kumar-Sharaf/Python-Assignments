""" Write a python script to create two Threads. First thread will print
all Even numbers and Second thread will print all Odd numbers till 100 """

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
T2.start()