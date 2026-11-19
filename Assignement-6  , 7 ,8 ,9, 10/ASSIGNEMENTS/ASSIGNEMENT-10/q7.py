# 7. Write a program to create a new list from existing list which contains cube of
# each number of list.

li=[1,22,33,11,44,55]
li1=[]
for i in li:
    if i not in li1:
        li1+=[i*i*i]
print(li1)

