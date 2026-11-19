# 6. Write a program to remove duplicates from the list.

li=[11,22,33,44,55,66,66,55]
li1=[]
for i in li:
    if i not in li1:
        li1+=[i]
print(li1)
