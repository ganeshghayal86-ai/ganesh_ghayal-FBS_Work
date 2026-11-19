# 13 . Write a program to print list after removing even numbers.

li=[31,42,63,85,72,95,40]
li1=[]
for i in li:
    if i not in li1:

        if i%2!=0:
            li1+=[i]
print(li1)