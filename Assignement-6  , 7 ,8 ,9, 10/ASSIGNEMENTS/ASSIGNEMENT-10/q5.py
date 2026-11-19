# 5. Accept a number from user and check if this element is present in the list or
# not. 

li=[12,33,45,67,88,11,1,2]
li.sort()
print(li)
start=0
end=len(li)-1
tar=int(input('enter number:'))
while start<=end:
    mid=(start+end)//2
    if tar==li[mid]:
        print('element is found')
        break
    elif tar>li[mid]:
        start=mid+1
    else:
        end=mid-1
else:
    print('element is not found')



