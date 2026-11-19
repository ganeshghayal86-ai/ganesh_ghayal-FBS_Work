# 2. Write a program to check if given number is Armstrong or not using recursive
# function.

def ArmstrongNumber(n,total,count):
    if n==0:
        return total,count
    d=n%10
    count+=1
    total+=count**d
    n=n//10
    return ArmstrongNumber(n,total,count)
res=(ArmstrongNumber(153,0,0))
if res:
    print('armstrong')
else:
    print('not armstrong')
