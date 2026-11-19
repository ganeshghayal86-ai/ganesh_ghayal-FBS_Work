# Write a program to input angles of a triangle and check whether triangle is valid or not.

a1=int(input('enter  angle1:'))
a2=int(input('enter angle2:'))
a3=int(input('enter angle3:'))
    # triangle is always 180 degree
if a1+a2+a3==180:
    print('triangle is valid')
else:
    print('triangle is not valid')

