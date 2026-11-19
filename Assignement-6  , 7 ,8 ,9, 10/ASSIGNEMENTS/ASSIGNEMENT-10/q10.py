# 10. Write a program to remove all occurrences of a given element in the list.

li=[11,11,11,23,34,45,6,74,6,23]
li1=[]
ele=int(input('enter element:'))
for i in li:
    if i not in li1:
        if i!=0:
            li1+=[i]
print(li1)
