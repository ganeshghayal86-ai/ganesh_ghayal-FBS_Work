# 7. Write a program to find sum of digits using recursion.

def SumOfDigits(n,sum):
    if n==0:
        return sum
    d=n%10
    sum+=d
    n=n//10
    return SumOfDigits(n,sum)
print(SumOfDigits(123456789,0))