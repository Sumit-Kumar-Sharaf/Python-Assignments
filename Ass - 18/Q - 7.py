"""Write a python program to create three dictionaries, then create one
dictionary that will contain the other three dictionaries"""

s1={"Name":"Sumit","Roll":17,"College":"R.R.K.G"}
s2={"Name":"Saroj","Roll":18,"College":"R.R.K.G"}
s3={"Name":"Saroj","Roll":16,"College":"R.R.K.G"}
student={1:s1,2:s2,3:s3}
for k in student:
    print(k,student[k])