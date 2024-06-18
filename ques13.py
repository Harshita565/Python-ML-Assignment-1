# Python Programming Assignment-1
# 13. Write a program that asks the user for their birth year and calculates their age.
import datetime
date = datetime.date.today()
year = int(date.year)
var = int(input("Enter your year of birth: "))
age = year-var
print(age)
