# 7. Write a program to find sum of digits of a number.
def SumOfDigitsOfNumber():
    n=int(input('enter numbers:'))
    total=0
    while n>0:
        digit=n%10
        total+=digit
        n=n//10
    print(total)
SumOfDigitsOfNumber()