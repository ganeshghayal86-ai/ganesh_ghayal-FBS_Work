# 4. WAP to print Armstrong number within a given range

num=int(input('enter number:'))
temp=num
total=0
count=0

n=num
while n>0:
    count+=1
    n=n//10
while num>0:
    digit=num%10
    total+=digit**count
    num=num//10


if total==temp:
    print('armstrong')
else:
    print('not armstrong')