""" Write a python script to create 5 threads to fill a list with random
numbers till 100 """

from threading import *
import random

def fill(list):
    while True:
        list.append(random.randint(1,100))
        if len(list)==50:
            break

list=[]
T1=Thread(target=fill,args=(list,))
T2=Thread(target=fill,args=(list,))
T1.start()
print(list)
