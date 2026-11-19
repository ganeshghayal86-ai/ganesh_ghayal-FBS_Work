# 9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

li=[11,22,33,44,55,66,77,88,99,100]
li1=[]
li2=[]
for i in li:
    if i not in li1:
        if i%2==0:
            li1+=[i]
        else:
            li2+=[i]
print(li1)
print(li2)
