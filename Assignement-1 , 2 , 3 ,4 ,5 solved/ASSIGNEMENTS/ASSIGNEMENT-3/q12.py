# 12. Write a program to check if given 3 digit number is a palindrome or not.

num=int(input('enter 3 digit number:'))
temp=num
d1=num%10
num//=10
d2=num%10
num//=10
d3=num%10
if (d1==d3):
    print('palindrom')
else:
    print('not palindrome')

