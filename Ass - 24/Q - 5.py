""" Write a python program to delete the age property of the user """

class person:
    def __init__(self):
        self.name="Sumit"
        self.age=20
        self.roll=17

p1=person()
print(p1.age)
del(p1.age)
print(p1.age)