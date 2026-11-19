# 1. Write a program to accept year from user and check if it is a leap year or not.

year=int(input('enter year:'))
if year%400==0 or (year%4==0 and year%100!=0):
    print('it is leap year')
else:
    print('it is not leap year')