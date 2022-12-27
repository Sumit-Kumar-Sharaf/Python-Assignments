""" Write a python script to create 2 threads to add all
the values from 1 to 100 """

from threading import *
def add():
    sum=0
    for i in range(101):
        sum=sum+i
    print(sum)
T1=Thread(target=add)
T1.start()
T2=Thread(target=add)
T2.start()