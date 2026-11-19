# 12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)

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


if total == temp:
    print('armstrong')
else:
    print('not armstrong')



