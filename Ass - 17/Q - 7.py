"""Write a python program to remove last item of the 
given set.
thisset = {"Python", "Django", "JavaScript", “SQL”}"""

thisset = {"Python", "Django", "JavaScript","SQL"}
thisset.remove("SQL")
thisset.discard("SQL")
print(thisset)