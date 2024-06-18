# Python Programming Assignment-1
# 18. Write a python program that checks if two strings are anagrams of each other. 
str1=input("Enter string1:")
set1= set(str1)
str2=input("Enter string2: ")
set2= set(str2)
if set1==set2:
    print("The two strings are anagrams")
else:
    print("They are not anagrams")