""" Define a class Employee with instance object variables empid, name, salary.
Write __init__() method in the class to initialize instance object variables.
Also define instance methods to input fields and display field values """

class Employee:
    def __init__(self) -> None:
        self.empid=0
        self.name="xyz"
        self.salary=0

    def set(self,id,name,sal):
        self.empid=id
        self.name=name
        self.salary=sal

    def get(self):
        print("Emp_ID : ",self.empid,"\nName : ",self.name,"\nSalary : ",self.salary,"\n")

e1=Employee()
e1.set(101,"Sumit",50000)
e1.get()