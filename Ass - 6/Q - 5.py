# Write a python script to print two given words in dictionary order.
text1=str(input("Enter A Word\n"))
text2=str(input("Enter A Word\n"))
if text1>text2:
    print(text2)
    print(text1)
else:
    print(text1)
    print(text2)