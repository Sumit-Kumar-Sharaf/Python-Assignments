""" Write a python program to create a function to check whether a
string is an anagram or not """

def isAnagram(str,word):
    s1=set(str.upper())
    s2=set(word.upper())
    if len(str)==len(word):
        if s1.issubset(s2):
            print("%s Is An Anagram String"%str)
        else:
            print("%s Is Not An Angaram String"%str)
    else:
            print("%s Is Not An Angaram String"%str)

isAnagram("Race","Care")