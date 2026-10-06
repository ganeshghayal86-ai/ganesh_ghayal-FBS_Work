# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a1=int(input('enter angle 1:'))
a2=int(input('enter angle 2:'))
a3=int(input('enter angle 3:'))

if a1==a2 and a2==a3:
    print('triangle is equilatral.')
elif a1==a2 or a2==a3 or a3==a1:
    print('triangle is isosceles.')
else:
    print('tringle is scalene')