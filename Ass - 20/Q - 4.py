""" Write a python program to create a function that checks whether a
passed string is palindrome or not """

def isPalindrome(str):
    str1=str[::-1]
    if(str==str1):
        print("%s Is A Plindrome String"%str)
    else:
        print("%s Is Not A Plindrome String"%str)

isPalindrome("radar")
isPalindrome("level")