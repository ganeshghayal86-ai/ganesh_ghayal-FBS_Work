# Write a program to reverse the list.

li=[22,12,33,55,11,1,2]
left=0
right=len(li)-1
while left<=right:
    li[left],li[right]=li[right],li[left]
    left+=1
    right-=1
print(li)