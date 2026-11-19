# 12. Write a program to create three lists of numbers, their squares
# and cubes


li=[12,33,52,11,10]
num=[]
li1=[]
li2=[]
for i in li:
        num+=[i]
        li1+=[i**2]
        li2+=[i*i*i]
print('number of list is:',num)
print('square of list is:',li1)
print('cube of list is:',li2)

   