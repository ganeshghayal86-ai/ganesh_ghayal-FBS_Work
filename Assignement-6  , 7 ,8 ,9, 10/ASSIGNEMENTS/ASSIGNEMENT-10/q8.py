# 8. Write a program to create a duplicate of an existing list. It should not point to
# same list.

li=[12,33,56,86,99]
li1=[]
for i in li:    
    if i  in li:
        li1+=[i]
print(li)
print(li1)