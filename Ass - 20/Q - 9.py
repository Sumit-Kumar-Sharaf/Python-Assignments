""" Write a python program to create a function to check whether a
string is a pangram or not """

def isPalindrome(s):
    str=s[::-1]
    if s==str:
        print("%s Is Palindrome"%s)
    else:
        print("%s Is Not Palindrome"%s)

isPalindrome("level")