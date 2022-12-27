'''Write a Python script to find if “Python” is present 
in the set thisset = {"Java","Python", "Django"}'''

thisset = {"Java","Python", "Django"}
for e in thisset:
    if e=="Python":
        print("Yes Python Is Present In This Set")
        break
else:
    print("No Python Is Not Present In This Set")