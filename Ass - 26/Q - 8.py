""" Write a python script to change the name of the Thread """

from threading import *

T1=Thread()
T1.name="1st Thread"
print(T1.name)