# Write a program to find the second largest element in the list.
li=[23,44,65,78,99,1,12]
largest=0
secondlargest=0
for i in li:
    if i>largest:
        secondlargest=largest
        largest=i
    elif i>secondlargest:
        secondlargest=i
print('second largest element of list is:',secondlargest)
