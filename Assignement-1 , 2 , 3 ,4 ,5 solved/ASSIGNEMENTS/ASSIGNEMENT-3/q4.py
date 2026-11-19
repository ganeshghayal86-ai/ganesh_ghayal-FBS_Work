# Write a program to input all sides of a triangle and check whether triangle is valid or not

a=int(input('enter side1:'))
b=int(input('enter side2:'))
c=int(input('enter side3:'))

if a+b>c and b+c>a and a+c>b:
    print('triangle is valid')
else:
    print ('triangle is not valid')