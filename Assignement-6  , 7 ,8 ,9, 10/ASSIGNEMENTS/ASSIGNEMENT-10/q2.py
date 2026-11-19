# Write a program to find maximum and minimum element in a list.

li=[12,11,77,55,45,100,]
largest=0
smallest=999
for i in li:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print('The maximum element of list is:',largest)
print('The minimum element of list is:',smallest)
